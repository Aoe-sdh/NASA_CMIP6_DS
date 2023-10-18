import shutil

import CIMP6_select
import os

path1 = 'F:/CMIP6/Merge'
path2 = 'F:/CMIP6/toSWATALL'
path3 = 'F:/CMIP6/toSWATALLUse'

variables = ["pr","ta","sfcWind","hurs","slr"]
scenarios = ["historical","ssp126", "ssp245","ssp370","ssp585"]


sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
            'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
           'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
           'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
           'NorESM2-LM', 'NorESM2-MM',"TaiESM1"]

for scenario in scenarios:
    for source in sources:
        p1 = path2 + "/" + scenario + "/" + source + "/"
        p2 = path3 + "/" + scenario + "/" + source + "/"
        if not os.path.exists(p2):
            CIMP6_select.mkdir(p2)

        list  = os.listdir(p1)
        for file in list:
            filename = p1 + file
            ret = "_" + scenario + "_" + source
            file1 = file.replace(ret,"")
            print(file1)
            fileout = p2 +file1
            # os.rename(filename,fileout)
            shutil.copyfile(filename, fileout)
        print(list)


