#

import os
import time
import numpy as np
import pandas as pd
# import climate_indices
from standard_precip import spi

from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import rpy2.robjects.numpy2ri as rpyn

def sub2db(subfile):
    if os.path.exists(subfile):
        names = ["NIGSUB", "SUB", "GIS", "MON", "AREA", "PRECIP", "SNOMELT","PET", "ET", "SW", "PREC", "SURQ", "GW_Q", "WYLD", "SYLD", "ORGN"
                   , "ORGP", "NSURQ", "SOLP", "SEDP", "LAT_Q", "LATNO3", "GWNO3", "CHOLA", "CBODU", "DOXQ", "TNO3", "QTILE", "TVAP", "YEAR"]
        subdata =pd.DataFrame(columns=names)
        Year = 2015
        with open(subfile) as infile:
            for _ in range(9):
                next(infile)
            for line in infile:
                splitted = []
                txt1 = line[0:6]   ### BIGSUB
                txt2 = line[6:11]   ### SUB
                txt3 = line[11:20]   ### GIS
                txt4 = line[20:25]   ### MON
                txt5 = line[25:35]   ### AREA
                txt6 = line[35:45]   ### PRECIP
                txt7 = line[45:55]   ### SNOMELT
                txt8 = line[55:65]   ### PET
                txt9 = line[65:75]   ### ET
                txt10 = line[75:85]   ### SW
                txt11 = line[85:95]   ### PREC
                txt12 = line[95:105]   ### SURQ
                txt13 = line[105:115]   ### GW_Q
                txt14 = line[115:125]   ### WYLD
                txt15 = line[125:135]   ### SYLD
                txt16 = line[135:145]   ### ORGN
                txt17 = line[145:155]   ### ORGP
                txt18 = line[155:165]   ### NSURQ
                txt19 = line[165:175]   ### SOLP
                txt20 = line[175:185]   ### SEDP
                txt21 = line[185:195]   ### LAT_Q
                txt22 = line[195:205]   ### LATNO5
                txt23 = line[205:215]   ### GWNO5
                txt24 = line[215:226]   ### CHOLA
                txt25 = line[226:236]   ### CBODU
                txt26 = line[236:246]   ### DOXQ
                txt27 = line[246:256]   ### TNO5
                txt28 = line[256:266]   ### QTILE
                txt29 = line[266:276]   ### TVAP

                splitted.append(txt1.strip())
                splitted.append(int(txt2.strip()))
                splitted.append(int(txt3.strip()))
                # print(txt1.strip(),txt2.strip(),txt3.strip(),txt4.strip(),txt5.strip(),txt6.strip(),txt7.strip()
                #       ,txt8.strip(),txt9.strip(),txt10.strip(),txt11.strip(),txt12.strip(),txt13.strip(),txt14.strip()
                # ,txt15.strip(),txt16.strip(),txt17.strip(),txt18.strip(),txt19.strip(),txt20.strip(),txt21.strip()
                #       ,txt22.strip(),txt23.strip(),txt24.strip(),txt25.strip(),txt26.strip(),txt27.strip(),txt28.strip()
                #       ,txt29.strip())
                splitted.append(int(txt4.strip()))
                splitted.append(float(txt3.strip()))
                splitted.append(float(txt6.strip()))
                splitted.append(float(txt7.strip()))
                splitted.append(float(txt8.strip()))
                splitted.append(float(txt9.strip()))
                splitted.append(float(txt10.strip()))
                splitted.append(float(txt11.strip()))
                splitted.append(float(txt12.strip()))
                splitted.append(float(txt13.strip()))
                splitted.append(float(txt14.strip()))
                splitted.append(float(txt15.strip()))
                splitted.append(float(txt16.strip()))
                splitted.append(float(txt17.strip()))
                splitted.append(float(txt18.strip()))
                splitted.append(float(txt19.strip()))
                splitted.append(float(txt20.strip()))
                splitted.append(float(txt21.strip()))
                splitted.append(float(txt22.strip()))
                splitted.append(float(txt23.strip()))
                splitted.append(float(txt24.strip()))
                splitted.append(float(txt25.strip()))
                splitted.append(float(txt26.strip()))
                splitted.append(float(txt27.strip()))
                splitted.append(float(txt28.strip()))
                splitted.append(float(txt29.strip()))

                mon = int(float(txt4.strip()))
                if mon <= 12:
                    splitted.append(Year)
                else:
                    Year = mon+1
                    splitted.append(mon)

                subdata=subdata.append(pd.DataFrame([splitted], columns=subdata.columns))


    else:
        print("Please check path:",subfile)
    return subdata

def read_outputSub(inpath):
    selpath = inpath + "Select"
    if os.path.isdir(selpath):
        exComd = "D:/PythonPrj/READ_SWAT_SUB/x64/Debug/READ_SWAT_SUB.exe " + inpath
        print(exComd)
        r_v = os.system(exComd)
        print(r_v)
    else:
        os.mkdir(selpath)
        exComd = "D:/PythonPrj/READ_SWAT_SUB/x64/Debug/READ_SWAT_SUB.exe " + inpath
        print(exComd)
        r_v = os.system(exComd)
        print(r_v)

    return

def read_pcp(infile):

    df = pd.read_csv(infile,index_col=False)
    print(df.columns)
    df["date"]= df[" YEAR"].astype(str) + "-"+df["MON"].astype(str).apply(lambda x:x.zfill(2))
    df["date"]=pd.to_datetime(df["date"])
    dfn=df[["date","PRECIP","PET","SW","WYLD"]]
    # print(dfn)
    return dfn

def calSPI(infile,itype):
    ####### standardized precipitation index
    try:
        print(infile)
        pcpTSeries = read_pcp(infile)
        spei = importr("SPEI")
        pandas2ri.activate()

        pcp = pcpTSeries["PRECIP"]
        # print(pcp)
        spi = spei.spi(pcp, itype)
        print(type(spi),"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        spin = pandas2ri.ri2py_vector(spi)
        print(type(spin),"***********************************************")

    except Exception as e:
        print("Check")


    return spin

def calSPEI(infile,itype):
    ####### standardized precipitation evapotranspiration index
    try:
        pcpTSeries = read_pcp(infile)
        spei = importr("SPEI")
        pandas2ri.activate()

        pcp = pcpTSeries["PRECIP"]
        pet = pcpTSeries["PET"]
        pcp = pcp -pet
        spei = spei.spei(pcp, itype)

    except Exception as e:
        print("Check")
    return spei

def calSSFI(infile,itype):
    #### standardized streamflow index
    try:
        pcpTSeries = read_pcp(infile)
        spei = importr("SPEI")
        pandas2ri.activate()

        pcp = pcpTSeries["WYLD"]
        ssfi = spei.spi(pcp, itype)

    except Exception as e:
        print("Check")
    return ssfi

def calSSMI(infile,itype):
    ##### standardized soil mositure index
    try:
        pcpTSeries = read_pcp(infile)
        spei = importr("SPEI")
        pandas2ri.activate()

        pcp = pcpTSeries["SW"]
        ssmi = spei.spi(pcp, itype)

    except Exception as e:
        print("Check")

    return ssmi
def calNEDI(infile):
    ########  normalized ecosystem drought index
    ###### the time lag is not considered
    pcpTSeries = read_pcp(infile)
    pcp = pcpTSeries["PRECIP"]
    pet = pcpTSeries["PET"]
    ww = pcp - pet
    wwmax = max(abs(ww))
    nedi = ww/wwmax
    return nedi

def calRDIe(infile):
    ###### modified reconnaissance drought index
    pcpTSeries = read_pcp(infile)
    pcp = pcpTSeries["PRECIP"]
    pet = pcpTSeries["PET"]
    ak = pcp / pet
    wwmean = ak.mean()
    rdie = ak/wwmean
    return rdie



if __name__ =="__main__":

    infile = "D:/PythonPrj/NASA_CMIP6_DS/Data/ACCESS-CM2/SELECT/0001_SUB_OUT.DAT"
    inpath = "D:/PythonPrj/NASA_CMIP6_DS/Data/ACCESS-CM2/"
    # # read_outputSub(inpath)
    tt1 = calSPI(infile, 1)
    # tt2 = calSPEI(infile, 1)
    # tt3 = calSSFI(infile, 1)
    # tt4 = calNEDI(infile)
    # tt5 = calRDIe(infile)
#######################    不知道怎么将 R的listVector转换为python 的数据类型 此方法暂时放弃

    print(type(tt1),tt1)
    print(tt1.tolist())

    # input = r"D:\PythonPrj\NASA_CMIP6_DS\Data\ACCESS-CM2\output.sub"
    # scenarios = ["historical", "ssp126", "ssp245", "ssp370", "ssp585"]
    # scenarios = ["ssp126"]
    # sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
    #            'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
    #            'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
    #            'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
    #            'NorESM2-LM', 'NorESM2-MM', "TaiESM1"]
    # pathi = "D:/PythonPrj/Data/"
    # patho = "D:/PythonPrj/Indice/"
    #
    # for scenario in scenarios:
    #     for source in sources:
    #         inpath = pathi + "Result_" + scenario + "/" + source + "/"
    #         outpath = patho + scenario + "/" + source + "/"
    #         folder = os.path.exists(outpath)
    #         if not folder:
    #             os.makedirs(outpath)
    #         read_outputSub(inpath)
    #         for sub in range(562):
    #             isub = sub + 1
    #             infile = inpath + str(isub).zfill(4) + "_SUB_OUT.DAT"
    #             outfile = outpath + str(isub).zfill(4) + "_SUB_OUT.DAT"
    #             spi = calSPI(infile, 1)
    #             spei = calSPEI(infile, 1)
    #             ssfi = calSSFI(infile, 1)
    #             ssmi = calSSMI(infile, 1)
    #             nedi = calNEDI(infile)
    #             rdie = calRDIe(infile)
    #
    #             dfindice = pd.concat([spi, spei, ssfi, ssmi, nedi, rdie],
    #                                  colums=["SPI", "SPEI", "SSFI", "SSMI", "NEDI", "RDIe"])
    #             dfindice.to_csv(outfile)
    #             time.sleep(10000)