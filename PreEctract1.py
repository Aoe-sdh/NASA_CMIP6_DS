import netCDF4 as nc
import pandas as pd
import numpy as np
import geopandas
from shapely.geometry import Point
from dbfread import DBF
import datetime
import shapely.geometry as geometry
import os
import sys
os.environ['PROJ_LIB'] = os.path.dirname(sys.argv[0])



file = 'F:/pre_0025_1.nc'
studyarea='E:/CMIP6/MLHJ_WatershedMerge_Buffer2h5km.shp'
area_shp = geopandas.GeoDataFrame.from_file(studyarea, encoding='utf-8')
region_shape = area_shp['geometry'][0]

dataset =nc.Dataset(file)
all_vars=dataset.variables.keys()
# print(all_vars)
#获取所有变量信息
all_vars_info = dataset.variables.items()
all_vars_info = list(all_vars_info)
# print(all_vars_info)
# 获取单独的一个变量的数据
Lat=dataset.variables['lat'][:]
Lon=dataset.variables['lon'][:]
Pre=dataset.variables['pre'][:]
time= dataset.variables['time']
# print(time)

# print(time1)
# print(ET.shape)
# 转换成数组
Pre_data = np.array(Pre)
Lat_data = np.array(Lat)
Lon_data = np.array(Lon)
Num_time = np.array(time)

flat_lon = Lon_data.flatten()  # 将坐标展成一维
flat_lat = Lat_data.flatten()

print(Pre_data.shape,Num_time.shape,Lat_data.shape,Lon_data.shape)


flat_points=[]
for i in range(int(flat_lon.shape[0])):
    for j in range(int(flat_lat.shape[0])):
        flat_points.append((flat_lon[i],flat_lat[j]))


in_shape_points = []
for pt in flat_points:
    # make a point and see if it's in the polygon
    xlon, ylat=pt

    if region_shape.contains(Point([xlon,ylat])):
        in_shape_points.append(pt)
    else:
        continue
selected_lon = [elem[0] for elem in in_shape_points]
selected_lat = [elem[1] for elem in in_shape_points]

preOut = []
for i in range(len(Num_time)):
    pre = 0.
    knum = 0
    for latj in range(len(Lat_data)):
        lat = Lat_data[latj]
        if lat in selected_lat:
            for lonj in range(len(Lon_data)):
                lon = Lon_data[lonj]
                if lon in selected_lon:
                    knum = knum +1
                    pre = pre + Pre_data[i, int(latj), int(lonj)]

    pre = pre / float(knum)
    preOut.append(pre)
test = pd.DataFrame(preOut)
test.to_csv('pre1.csv')




