import CIMP6_select
import os
import netCDF4 as nc

path1 = 'F:/CMIP6/Merge'
path2 = 'F:/CMIP6/toSWATALL'


variables = ["pr","ta","sfcWind","hurs","slr"]
scenarios = ["historical","ssp126", "ssp245","ssp370","ssp585"]
scenarios = ["historical","ssp126"]

sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
            'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
           'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
           'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
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

                if variable == "ta" or variable == "slr":
                    dataset1 = nc.Dataset(p31)
                    dataset2 = nc.Dataset(p32)
                    lat_set = dataset1.variables['lat'][:]
                    lon_set = dataset1.variables['lon'][:]
                    temp_set1 = dataset1.variables[var[0]][:]
                    temp_set2 = dataset2.variables[var[1]][:]
                    time_set = dataset1.variables['time'][:]
                    if variable == "ta":
                        temp_set1 = temp_set1 - 273.15
                        temp_set2 = temp_set2 - 273.15
                    else:
                        temp_set1 = temp_set1 * 86400 / 1000000
                        temp_set2 = temp_set2 * 86400 / 1000000
                else:
                    dataset = nc.Dataset(p3)
                    lat_set = dataset.variables['lat'][:]
                    lon_set = dataset.variables['lon'][:]
                    temp_set = dataset.variables[variable][:]
                    time_set = dataset.variables['time'][:]
                    if variable == "pr":
                        temp_set = temp_set * 86400
                    elif variable == "hurs":
                        temp_set = temp_set / 100


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
                            for i in range(len(time_set)):

                               if variable == "ta" or variable == "slr":
                                  if variable == "ta":
                                      tem1 = "{:.2f}".format(temp_set1[i][j][k])
                                      tem2 = "{:.2f}".format(temp_set2[i][j][k])
                                      temta = tem2+ ","+tem1
                                      f.write(temta + "\n")

                                  else:
                                      # tem = "{:.2f}".format(temp_set2[i][j][k]+temp_set1[i][j][k])
                                      tem = "{:.2f}".format(temp_set1[i][j][k])

                                      f.write(tem +"\n")
                               else:
                                  tem = "{:.2f}".format(temp_set[i][j][k])
                                  f.write(tem + "\n")

                       # with open(file_name + '.csv', 'w', newline='') as targetFile:
                       #      ## 创建写入流
                       #      writer = csv.writer(targetFile)
                       #      ## 写入表头
                       #      # if "historical" in file_name:
                       #      #     writer.writerow(('"19500101"'))
                       #      # else:
                       #      #     writer.writerow(('"20150101"'))
                       #
                       #      ## 写入数据
                       #      for i in range(len(time_set)):
                       #
                       #           temp = temp_set[i][j][k]
                       #           if variable == "ta" or variable == "slr":
                       #               if variable == "ta":
                       #                   writer.writerow((temp_set2[i][j][k],temp_set1[i][j][k]))
                       #               else:
                       #                   writer.writerow((temp_set2[i][j][k]+temp_set1[i][j][k]))
                       #           else:
                       #               writer.writerow(temp)