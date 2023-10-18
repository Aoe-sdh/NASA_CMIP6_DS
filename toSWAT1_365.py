import time

import CIMP6_select
import os
import netCDF4 as nc
import pandas as pd
import numpy as np

path1 = 'G:/CMIP6/Merge'
path2 = 'G:/CMIP6/toSWATALL'


variables = ["pr","ta","sfcWind","hurs","slr"]
scenarios = ["historical","ssp126", "ssp245","ssp370","ssp585"]
# scenarios = ["ssp126", "ssp245","ssp370","ssp585"]

sources = ['CanESM5','CMCC-ESM2',
           'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
           'NorESM2-LM', 'NorESM2-MM',"TaiESM1"]


for scenario in scenarios:
     for source in sources:
          print(source)
          for variable in variables:
                p1 = path1 + "/" + scenario + "/" + source + "/"
                p2 = path2 + "/" + scenario + "/" + source
                if variable == "ta" or variable == "slr" :
                    if variable == "ta":
                        var = ["tasmax","tasmin"]
                    else:
                        var = ["rsds", "rlds"]
                    p31 = path1 + "/" + scenario + "/" + source + "/" + var[0] + "_" + scenario + "_" + source + ".nc"
                    p32 = path1 + "/" + scenario + "/" + source + "/" + var[1] + "_" + scenario + "_" + source + ".nc"

                else:
                    p3 = path1 + "/" + scenario + "/" + source + "/" + variable + "_" + scenario + "_" + source + ".nc"

                p4 = path2 + "/" + scenario + "/" + source + "/" + variable + "_" + scenario + "_" + source

                if not os.path.exists(p2):
                    CIMP6_select.mkdir(p2)


                if scenario =="historical":
                    date_range = pd.date_range(start="1950-01-01", end="2014-12-31", freq="D")  # freq="D"表示按天，可以按分钟，月，季度，年等
                else:
                    date_range = pd.date_range(start="2015-01-01", end="2100-12-31", freq="D")  # freq="D"表示按天，可以按分钟，月，季度，年等

                if variable == "ta" or variable == "slr":
                    dataset1 = nc.Dataset(p31)
                    dataset2 = nc.Dataset(p32)
                    lat_set = dataset1.variables['lat'][:]
                    lon_set = dataset1.variables['lon'][:]
                    temp_set1 = dataset1.variables[var[0]][:]
                    temp_set2 = dataset2.variables[var[1]][:]
                    time_set = dataset1.variables['time']
                    time1 = nc.num2date(time_set, time_set.units, time_set.calendar).data

                    if variable == "ta":
                        temp_set1 = temp_set1 - 273.15
                        temp_set2 = temp_set2 - 273.15
                    else:
                        temp_set1 = temp_set1 * 86400 / 1000000
                        temp_set2 = temp_set2 * 86400 / 1000000
                    for i in range(len(time1)):
                        Year = time1[i].year
                        Month = time1[i].month
                        Day = time1[i].day
                        date_365 = str(Year) + "-" + str(Month).zfill(2) + "-" + str(Day).zfill(2)
                        Date365.append(date_365)
                    df_temp = pd.DataFrame(list(zip(Date365, temp_set1.tolist(),temp_set2.tolist())), columns=["Date", "temp_set1", "temp_set2"])
                    df_temp["Date"] = pd.to_datetime(df_temp["Date"])
                    df_temp = df_temp.set_index("Date").reindex(index=date_range)
                    df_temp1 = df_temp.fillna(method="ffill")
                    temp_setN1 = np.array(df_temp1["temp_set1"].to_list())
                    temp_setN2 = np.array(df_temp1["temp_set2"].to_list())

                else:
                    dataset = nc.Dataset(p3)
                    lat_set = dataset.variables['lat'][:]
                    lon_set = dataset.variables['lon'][:]
                    temp_set = dataset.variables[variable][:]
                    time_set = dataset.variables['time']
                    time1 = nc.num2date(time_set, time_set.units, time_set.calendar).data
                    if variable == "pr":
                        temp_set = temp_set * 86400
                    elif variable == "hurs":
                        temp_set = temp_set / 100
                    Date365 = []
                    for i in range(len(time1)):
                        Year = time1[i].year
                        Month = time1[i].month
                        Day = time1[i].day
                        date_365 = str(Year) + "-" + str(Month).zfill(2) + "-" + str(Day).zfill(2)
                        Date365.append(date_365)
                    df_temp = pd.DataFrame(list(zip(Date365, temp_set.tolist())), columns=["Date", "temp_set"])
                    df_temp["Date"] = pd.to_datetime(df_temp["Date"])
                    df_temp = df_temp.set_index("Date").reindex(index=date_range)
                    df_temp1 = df_temp.fillna(method="ffill")
                    temp_setN = np.array(df_temp1["temp_set"].to_list())

                file_name0 = p4
                # for j in range(len(lat_set)):  # j为纬度
                #     for k in range(len(lon_set)):  # k为经度
                for j in range(4,20):  # j为纬度
                    for k in range(16,33):  # k为经度
                       file_name = file_name0 + "_lat" + str(j).zfill(3) + "_lon" + str(k).zfill(3)

                       with open(file_name + '.txt', 'w') as f:
                            if "historical" in file_name:
                                f.write("19500101" + "\n")
                            else:
                                f.write("20150101" + "\n")
                            for i in range(len(date_range)):

                               if variable == "ta" or variable == "slr":
                                  if variable == "ta":
                                      tem1 = "{:.2f}".format(temp_setN1[i][j][k])
                                      tem2 = "{:.2f}".format(temp_setN2[i][j][k])
                                      temta = tem2+ ","+tem1
                                      f.write(temta + "\n")

                                  else:
                                      # tem = "{:.2f}".format(temp_set2[i][j][k]+temp_set1[i][j][k])
                                      tem = "{:.2f}".format(temp_setN1[i][j][k])

                                      f.write(tem +"\n")
                               else:
                                  tem = "{:.2f}".format(temp_setN[i][j][k])
                                  f.write(tem + "\n")