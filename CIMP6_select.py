import numpy as np
import netCDF4 as nc
import xarray as xr
import os
import tools


def cmip6Clip(file_xadv,path1,path2,value):

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



def mkdir(path):
     folder = os.path.exists(path)

     if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
          os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
          print("---  new folder...  OK---")
     else:
          print("---  There is this folder!  ---")



path1 = 'F:/ClimateDataChinaClip'
path2 = 'F:/CMIP6_R'
path3 = 'F:/CMIP6_R_Select'
# path3 = "C:\\zxDownscale\\BiasCorrec\\Data\\CMIP6_Select"
shapefile = 'C:/zxDownscale/01NCClip/Data/Zone02.shp'

variables = ["pr","tasmax","tasmin"]
scenarios = ["historical","ssp126", "ssp245","ssp370","ssp585"]
sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'AWI-CM-1-1-MR',
           'BCC-CSM2-MR', 'CanESM5', 'CESM2', 'CESM2-WACCM',
           'CMCC-CM2-SR5', 'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg',
           'FGOALS-g3', 'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0', 'IPSL-CM6A-LR',
           'MIROC6', 'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0', 'NorESM2-LM', 'NorESM2-MM']


for variable in variables:
     for scenario in scenarios:
          for source in sources:
               file_xadv = []
               p1 = path1 + "/" +variable +"/" +scenario +"/" +source +"/"

               if os.path.exists(p1):
                    file_xadv = os.listdir(p1)
                    p2 = path2 + "/" +variable +"/" +variable +"_"+scenario +"_" +source +".nc"
                    p3 = path2 + "/" +variable
                    if not os.path.exists(p3):
                         mkdir(p3)
                    if not os.path.exists(p2):
                         try:
                              cmip6Merge(file_xadv,p1,p2,variable)
                         except Exception as e:
                              continue
                    p4 = path3 + "/" +variable
                    if not os.path.exists(p4):
                         mkdir(p4)
                    p5 = path3 + "/" + variable + "/" + variable + "_" + scenario + "_" + source + "_1980-2014.nc"
                    p6 = path3 + "/" + variable + "/" + variable + "_" + scenario + "_" + source + "_2015-2100.nc"

                    if scenario == "historical":
                         if not os.path.exists(p5):
                              try:
                                   cmip6TimeSelect(p2,variable,p5,"0")
                              except Exception as e:
                                   continue
                    else:
                         if not os.path.exists(p6):
                              try:
                                   cmip6TimeSelect(p2,variable,p6,"1")
                              except Exception as e:
                                   continue







