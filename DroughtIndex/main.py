import os
import time

import pandas as pd
import Tools
from standard_precip.spi import SPI

def read_pcp(infile):

    df = pd.read_csv(infile,index_col=False)
    print(df.columns)
    df["date"]= df[" YEAR"].astype(str) + "-"+df["MON"].astype(str).apply(lambda x:x.zfill(2))
    df["date"]=pd.to_datetime(df["date"])
    dfn=df[["date","PRECIP","PET","SW","WYLD"]]
    # print(dfn)
    return dfn
def calSPI_M(infile,itype):
    pcpTSeries = read_pcp(infile)
    pcpTSeries["SPEI"] = pcpTSeries["PRECIP"] -pcpTSeries["PET"]

    spi = SPI()
    df_spi = spi.calculate(
        pcpTSeries,
        'date',
        'PRECIP',
        freq="M",
        scale=itype,
        fit_type="lmom",
        dist_type="gam"
    )
    df_spei = spi.calculate(
        pcpTSeries,
        'date',
        'SPEI',
        freq="M",
        scale=itype,
        fit_type="mle",
        dist_type="gam"
    )

    df_ssfi = spi.calculate(
        pcpTSeries,
        'date',
        'WYLD',
        freq="M",
        scale=itype,
        fit_type="mle",
        dist_type="exp"
    )

    df_ssmi = spi.calculate(
        pcpTSeries,
        'date',
        'SW',
        freq="M",
        scale=itype,
        fit_type="lmom",
        dist_type="gam"
    )

    ispi = df_spi["PRECIP_calculated_index"]
    ispei = df_spei["SPEI_calculated_index"]
    issfi = df_ssfi["WYLD_calculated_index"]
    issmi = df_ssmi["SW_calculated_index"]
    return ispi,ispei,issfi,issmi

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





if __name__=="__main__":
    input = r"D:\PythonPrj\NASA_CMIP6_DS\Data\ACCESS-CM2\output.sub"
    scenarios = ["historical", "ssp126", "ssp245", "ssp370", "ssp585"]
    scenarios = ["ssp126"]
    sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
               'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
               'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
               'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
               'NorESM2-LM', 'NorESM2-MM', "TaiESM1"]
    pathi = "D:/PythonPrj/Data/"
    patho = "D:/PythonPrj/Indice/"


#######  生成 各 Sub单独文件
    # for scenario in scenarios:
    #     for source in sources:
    #         inpath = pathi +"Result_"+ scenario + "/" + source + "/"
    #         outpath = patho + scenario + "/" + source + "/"
    #         folder = os.path.exists(outpath)
    #         if not folder:
    #             os.makedirs(outpath)
    #         Tools.read_outputSub(inpath)

    for scenario in scenarios:
        for source in sources:
            inpath = pathi + "Result_" + scenario + "/" + source + "/"
            outpath = patho + scenario + "/" + source + "/"
            for sub in range(562):
                isub = sub +1
                infile = inpath + "SELECT/"+str(isub).zfill(4) + "_SUB_OUT.DAT"
                outfile = outpath + str(isub).zfill(4) + "_SUB_OUT.DAT"
                spi = calSPI_M(infile, 1)
                # spei = Tools.calSPEI(infile, 1)
                # ssfi = Tools.calSSFI(infile, 1)
                # ssmi = Tools.calSSMI(infile, 1)
                # nedi = Tools.calNEDI(infile)
                # rdie = Tools.calRDIe(infile)
                # print(type(spi),"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                # dfindice = pd.concat([spi,spei,ssfi,ssmi,nedi,rdie])
                #
                # dfindice.columns = ["SPI", "SPEI", "SSFI", "SSMI", "NEDI", "RDIe"]
                # dfindice.to_csv(outfile)
                time.sleep(10000)




