import xarray
import rioxarray
import geopandas
from shapely.geometry import mapping
import pyproj
import logging
import netCDF4
import numpy


# shapefile = 'C:/zxDownscale/01NCClip/Data/Country.shp'
# originalfile = 'C:/zxDownscale/01NCClip/Data/clt_day_ACCESS-CM2_historical_r1i1p1f1_gn_19500101-19991231.nc'
# variable='clt'
# outfile="C:/zxDownscale/01NCClip/Data/test3.nc"


def nc_clip(shapefile, originalfile, outfile, variable):

    # pyproj.datadir.set_data_dir(r"C:/ProgramData/Anaconda3/envs/geo_env/Lib/site-packages/pyproj/proj_dir/share/proj")
    xds = xarray.open_dataset(originalfile,)
    xds = xds[[variable]].transpose('time', 'lat', 'lon')
    xds.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
    xds.rio.write_crs('EPSG:4326', inplace=True)
    geodf = geopandas.read_file(shapefile)
    clipped = xds.rio.clip(geodf.geometry.apply(mapping), geodf.crs)
    clipped.to_netcdf(outfile)
    logging.basicConfig(level=logging.INFO,
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
    logging.info(outfile)
# nc_clip(shapefile, originalfile, outfile, variable)

def ncmerge(input,output):
    ds = xarray.open_mfdataset(input, combine="by_coords", concat_dim="time")
    ds.to_netcdf(output)