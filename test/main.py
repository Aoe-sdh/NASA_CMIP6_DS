import CIMP6_select
import os

path1 = 'F:/CMIP6/Data'
path2 = 'F:/CMIP6/Merge'
path3 = 'F:/CMIP6_R_Select'

variables = ["pr","tasmax","tasmin","sfcWind","rsds","hurs","rlds"]
scenarios = ["historical","ssp126", "ssp245","ssp370","ssp585"]
scenarios = ["ssp585"]

sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
            'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
           'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
           'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
           'NorESM2-LM', 'NorESM2-MM',"TaiESM1"]
sources = ["TaiESM1"]

time1=[i for i in  range(1950,2015,1)]     ##### historical  1950 2014 ; ssp  2015 2100
time2=[i for i in  range(2015,2101,1)]


for scenario in scenarios:
     for source in sources:
          for variable in variables:
                file_xadv = []

                p1 = path1 + "/" +scenario +"/" +source +"/"
                p2 = path2 + "/" + scenario + "/" + source
                p3 = path2 + "/" +scenario +"/" +source +"/" +variable +"_"+scenario +"_" +source +".nc"

                if os.path.exists(p1):
                     files = os.listdir(p1)
                     for file in files:
                          if variable in file:

                              file_xadv.append(file)
                              # print(file)

                if scenario == "historical":

                    if len(file_xadv) == 65:
                        if not os.path.exists(p2):
                            CIMP6_select.mkdir(p2)

                        CIMP6_select.cmip6Merge(file_xadv, p1, p3, variable)
                    else:
                        print("Please check ",variable,p1)
                else:
                    if len(file_xadv) == 86:
                        if not os.path.exists(p2):
                            CIMP6_select.mkdir(p2)

                        CIMP6_select.cmip6Merge(file_xadv, p1, p3, variable)
                    else:
                        print("Please check ",p1)
                # print("################################")
                # if not os.path.exists(p2):
                #     CIMP6_select.mkdir(p2)
                # # try:
                # print("################################")
                # cmip6Merge(file_xadv, p1, p3, variable)
                # except Exception as e:
                #      continue
                         # p2 = path2 + "/" +variable +"/" +variable +"_"+scenario +"_" +source +".nc"
                         # p3 = path2 + "/" +variable
                         # if not os.path.exists(p3):
                         #      mkdir(p3)
                         # if not os.path.exists(p2):
                         #      try:
                         #           cmip6Merge(file_xadv,p1,p2,variable)
                         #      except Exception as e:
                         #           continue
                         # p4 = path3 + "/" +variable
                         # if not os.path.exists(p4):
                         #      mkdir(p4)
                         # p5 = path3 + "/" + variable + "/" + variable + "_" + scenario + "_" + source + "_1980-2014.nc"
                         # p6 = path3 + "/" + variable + "/" + variable + "_" + scenario + "_" + source + "_2015-2100.nc"
                         #
                         # if scenario == "historical":
                         #      if not os.path.exists(p5):
                         #           try:
                         #                cmip6TimeSelect(p2,variable,p5,"0")
                         #           except Exception as e:
                         #                continue
                         # else:
                         #      if not os.path.exists(p6):
                         #           try:
                         #                cmip6TimeSelect(p2,variable,p6,"1")
                         #           except Exception as e:
                         #                continue

for scenario in scenarios:
     for source in sources:
          for variable in variables:
                file_xadv = []

                p1 = path1 + "/" +scenario +"/" +source +"/"
                p2 = path2 + "/" + scenario + "/" + source
                p3 = path2 + "/" +scenario +"/" +source +"/" +variable +"_"+scenario +"_" +source +".nc"