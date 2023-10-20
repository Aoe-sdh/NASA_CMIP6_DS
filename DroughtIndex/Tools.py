#

import os
import pandas as pd
import climate_indices
from standard_precip import spi

from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
def read_outputSub(inpath):
    selpath = inpath + "Select"
    if os.path.isdir(selpath):
        exComd = "D:/PythonPrj/READ_SWAT_SUB/x64/Debug/READ_SWAT_SUB.exe " + inpath
        print(exComd)
        r_v = os.system(exComd)
        print(r_v)
    else:
        os.mkdir(selpath)

    return

def read_pcp(infile):

    df = pd.read_csv(infile,index_col=False)
    print(df.columns)
    df["date"]= df[" YEAR"].astype(str) + "-"+df["MON"].astype(str).apply(lambda x:x.zfill(2))
    df["date"]=pd.to_datetime(df["date"])
    dfn=df[["date","PRECIP"]]
    print(dfn)
    return dfn

if __name__ =="__main__":

    infile = "D:/PythonPrj/NASA_CMIP6_DS/Data/ACCESS-CM2/SELECT/0001_SUB_OUT.DAT"
    inpath = "D:/PythonPrj/NASA_CMIP6_DS/Data/ACCESS-CM2/"
    # read_outputSub(inpath)
    for i in range(30):
        try:
            pcpTSeries = read_pcp(infile)
            spei = importr("SPEI")
            pandas2ri.activate()

            pcp = pcpTSeries["PRECIP"]
            tt=spei.spei(pcp,1)

        except Exception as e:
            print("Check")

        print(i,"end")
