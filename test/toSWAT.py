import CIMP6_select
import os

path1 = 'F:/CMIP6/Merge'
path2 = 'F:/CMIP6/toSWAT'
path3 = 'F:/CMIP6_R_Select'

variables = ["pr","tasmax","tasmin","sfcWind","rsds","hurs","rlds"]
scenarios = ["historical","ssp126", "ssp245","ssp370","ssp585"]
sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
            'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
           'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
           'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
           'NorESM2-LM', 'NorESM2-MM',"TaiESM1"]


for scenario in scenarios:
     for source in sources:
          for variable in variables:
                p1 = path1 + "/" + scenario + "/" + source + "/"
                p2 = path2 + "/" + scenario + "/" + source
                p3 = path1 + "/" + scenario + "/" + source + "/" + variable + "_" + scenario + "_" + source + ".nc"
                p4 = path2 + "/" + scenario + "/" + source + "/" + variable + "_" + scenario + "_" + source
                if not os.path.exists(p2):
                    CIMP6_select.mkdir(p2)

                CIMP6_select.cimp6toSWAT(p3, p4, variable)