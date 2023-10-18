import numpy as np
import xarray as xr
import rioxarray
import geopandas
from shapely.geometry import mapping
import matplotlib.pyplot as plt

data = xr.open_dataset('C:/Users/a/Downloads/pre_0025_1.nc')
fig = plt.figure(figsize=(40,30))
data.tasmax[0].plot()
plt.show()

# shp = geopandas.read_file('D:/Ori_data/Poly/Afc.shp')
# data.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
# data.rio.write_crs("WGS1984", inplace=True)#视自己的数据坐标系而定，这里是比较广泛的WGS1984
# clipped = data.rio.clip(shp.geometry.apply(mapping), shp.crs)
# #clipped.to_netcdf('dir+name.nc')#将裁剪后的nc文件保存
# clipped.Q[0].plot()#同样选择时间序列上第一条数据进行展示