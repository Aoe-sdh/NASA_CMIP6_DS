import netCDF4 as nc
import xarray as xr
import os
import tools
import csv


def cmip6Clip(shapefile,file_xadv,path1,path2,value):

     for i in range(len(file_xadv)):
          outfile = path2 + file_xadv[i]
          orifile = path1 + file_xadv[i]
          print(orifile,outfile)
          tools.nc_clip(shapefile, orifile, outfile, value)

def cmip6Merge(file_xadv, path1, fileout,value):
     hadv_new = []



     for i in range(len(file_xadv)):
          xadv=xr.open_dataset(path1+file_xadv[i])[value]
          hadv_new.append((xadv))
          print(file_xadv[i])
     da=xr.concat(hadv_new,dim='time')
     da.to_netcdf(fileout)#输出合并后的nc文件

def cmip6TimeSelect(file,varible,fileout,Dtype):
     nc = xr.open_dataset(file)
     v = nc[varible]  # prec为变量内容（降雨）
     if Dtype == "1" :    ######  0 为历史，1为预测
          nc_30 = v.loc['2015-01-01':'2100-12-31']  # 截取时间
     elif Dtype == "0":
          nc_30 = v.loc['1980-01-01':'2014-12-31']  # 截取时间
     if varible == "pr":
          nc_30 = nc_30 * 86400.
     else:
          nc_30 = nc_30 - 273.15
     nc_30.to_netcdf(fileout)
     print('###### success #####', fileout)


def cimp6toSWAT(path,outpath,variible):

     file = path
     dataset = nc.Dataset(file)
     lat_set = dataset.variables['lat'][:]
     lon_set = dataset.variables['lon'][:]
     temp_set = dataset.variables[variible][:]
     time_set = dataset.variables['time'][:]

     if variible == "pr":
          temp_set = temp_set * 86400
     elif variible == "hurs":
          temp_set = temp_set / 100
     elif variible == "rsds" or variible == "rlds":
          temp_set = temp_set * 86400 / 1000000
     else:
          temp_set = temp_set -273.15

     source_file = file.split('.')
     file_name0 = outpath
     for j in range(len(lat_set)):  # j为纬度
          for k in range(len(lon_set)):  # k为经度
               file_name = file_name0 + "_lat" + str(j).zfill(3) + "_lon" + str(k).zfill(3)
               with open(file_name + '.csv', 'w', newline='') as targetFile:
                    # 创建写入流
                    writer = csv.writer(targetFile)
                    # 写入表头
                    writer.writerow(('time', 'lat', 'lon', variible))
                    # 写入数据
                    for i in range(len(time_set)):
                         writer.writerow((time_set[i], lat_set[j], lon_set[k],temp_set[i][j][k]))







def mkdir(path):
     folder = os.path.exists(path)

     if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
          os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
          print("---  new folder...  OK---")
     else:
          print("---  There is this folder!  ---")