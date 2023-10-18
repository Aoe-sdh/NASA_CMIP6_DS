import datetime
import time
import pandas as pd
import CIMP6_select
import os

def tranfPcp(pathdef,pathscn,pathSwat,secnario,source):
    print("TransF: pr_", secnario, source)
    filepcp = pathdef + "pcp1.pcp"
    fpcp = open(filepcp, "r")
    linespcp = fpcp.readlines()
    spcp = linespcp[0]
    lstspcp = spcp.split(",")
    locations = []
    for lst in lstspcp:
        locations.append(lst[-14:])

    file = pathscn + "pr_"+secnario+"_"+source + locations[0] + ".txt"
    fdata = pd.read_csv(file)
    timestart = fdata.columns[0]
    fdata.columns = [locations[0]]
    startY = timestart[:4]
    startM = timestart[4:6]
    startD = timestart[6:8]

    for loca in locations[1:-1]:
        file = pathscn + "pr_"+secnario+"_"+source  + loca + ".txt"
        data = pd.read_csv(file)
        data.columns = [loca]
        fdata = pd.concat([fdata, data], axis=1)

    pcps = []
    pcps.append(linespcp[0][0:-2])
    pcps.append(linespcp[1][0:-2])
    pcps.append(linespcp[2][0:-2])
    pcps.append(linespcp[3][0:-2])
    # print(pcps)
    datestart = startY + "-" + startM + "-" + startD
    time0 = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    timei = time0

    timein = []
    for i in fdata.index:
        Year = timei.year
        dateidlt = str(Year) + "-01-01"
        timeidlt = datetime.datetime.strptime(dateidlt, '%Y-%m-%d')
        dlt = (timei - timeidlt).days+1
        timei = timei + datetime.timedelta(days=1)
        txt = str(Year) + str(dlt).zfill(3)
        timein.append(txt)
    # print(timein)

    fdata1 = fdata.apply(lambda x: round(x, 1), axis=1)
    fdata1 = fdata1.applymap(str)
    fdata1 = fdata1.applymap(lambda x: x.zfill(5))
    fdata1.insert(0, "timein", timein)
    fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
    tt = fdata1["contact"].to_list()
    pcps.extend(tt)
    pcpdf = pd.DataFrame(pcps)
    pcpdf.to_csv(pathSwat + "pcp1.pcp", index=None, header=None)

def tranfTmp(pathdef,pathscn,pathSwat,secnario,source):
    print("TransF: ta_", secnario, source)
    filetmp = pathdef + "pcp1.pcp"
    ftmp = open(filetmp, "r")
    linestmp = ftmp.readlines()
    stmp = linestmp[0]
    lststmp = stmp.split(",")
    locations = []
    for lst in lststmp:
        locations.append(lst[-14:])


    file = pathscn + "ta_"+secnario+"_"+source + locations[0] + ".txt"
    fdata0 = pd.read_csv(file)
    timestart = fdata0.columns[0]
    startY = timestart[:4]
    startM = timestart[4:6]
    startD = timestart[6:8]

    file = pathscn + "ta_"+secnario+"_"+source + locations[0] + ".txt"
    fdata = pd.read_csv(file, skiprows=1, names=[locations[0] + "min", locations[0] + "max"])

    df = pd.DataFrame
    for loca in locations[1:-1]:
        file = pathscn + "ta_"+secnario+"_"+source + loca + ".txt"
        data = pd.read_csv(file, skiprows=1, names=[loca + "min", loca + "max"])
        fdata = pd.concat([fdata, data], axis=1)

    tmps = []
    tmps.append(linestmp[0][0:-2])
    tmps.append(linestmp[1][0:-2])
    tmps.append(linestmp[2][0:-2])
    tmps.append(linestmp[3][0:-2])
    # print(tmps)
    datestart = startY + "-" + startM + "-" + startD
    time0 = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    timei = time0

    timein = []
    for i in fdata.index:
        Year = timei.year
        dateidlt = str(Year) + "-01-01"
        timeidlt = datetime.datetime.strptime(dateidlt, '%Y-%m-%d')
        dlt = (timei - timeidlt).days+1
        timei = timei + datetime.timedelta(days=1)
        txt = str(Year) + str(dlt).zfill(3)
        timein.append(txt)
    # print(timein)

    fdata1 = fdata.apply(lambda x: round(x, 1), axis=1)
    fdata1 = fdata1.applymap(str)
    fdata1 = fdata1.applymap(lambda x: x.zfill(5))
    fdata1.insert(0, "timein", timein)
    fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
    tt = fdata1["contact"].to_list()
    tmps.extend(tt)
    pcpdf = pd.DataFrame(tmps)
    pcpdf.to_csv(pathSwat + "tmp1.tmp", index=None, header=None)

def tranfHmd(pathdef,pathscn,pathSwat,secnario,source):
    print("TransF: hurs_", secnario, source)
    filepcp = pathdef + "pcp1.pcp"
    fpcp = open(filepcp, "r")
    linespcp = fpcp.readlines()
    spcp = linespcp[0]
    lstspcp = spcp.split(",")
    locations = []
    for lst in lstspcp:
        locations.append(lst[-14:])

    file = pathscn + "hurs_"+secnario+"_"+source + locations[0] + ".txt"
    fdata = pd.read_csv(file)
    timestart = fdata.columns[0]
    fdata.columns = [locations[0]]
    startY = timestart[:4]
    startM = timestart[4:6]
    startD = timestart[6:8]

    for loca in locations[1:-1]:
        file = pathscn + "hurs_"+secnario+"_"+source + loca + ".txt"
        data = pd.read_csv(file)
        data.columns = [loca]
        fdata = pd.concat([fdata, data], axis=1)

    pcps = []
    pcps.append(linespcp[0][0:-2])
    # print(pcps)
    datestart = startY + "-" + startM + "-" + startD
    time0 = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    timei = time0

    timein = []
    for i in fdata.index:
        Year = timei.year
        dateidlt = str(Year) + "-01-01"
        timeidlt = datetime.datetime.strptime(dateidlt, '%Y-%m-%d')
        dlt = (timei - timeidlt).days+1
        timei = timei + datetime.timedelta(days=1)
        txt = str(Year) + str(dlt).zfill(3)
        timein.append(txt)
    # print(timein)

    fdata1 = fdata.applymap(lambda x: f"%.3f" % x)
    fdata1 = fdata1.applymap(str)
    fdata1 = fdata1.applymap(lambda x: x.zfill(8))
    fdata1.insert(0, "timein", timein)
    fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
    tt = fdata1["contact"].to_list()
    pcps.extend(tt)
    pcpdf = pd.DataFrame(pcps)
    pcpdf.to_csv(pathSwat + "hmd.hmd", index=None, header=None)

def tranfSlr(pathdef,pathscn,pathSwat,secnario,source):
    print("TransF: slr_", secnario, source)
    filepcp = pathdef + "pcp1.pcp"
    fpcp = open(filepcp, "r")
    linespcp = fpcp.readlines()
    spcp = linespcp[0]
    lstspcp = spcp.split(",")
    locations = []
    for lst in lstspcp:
        locations.append(lst[-14:])

    file = pathscn + "slr_"+secnario+"_"+source + locations[0] + ".txt"
    fdata = pd.read_csv(file)
    timestart = fdata.columns[0]
    fdata.columns = [locations[0]]
    startY = timestart[:4]
    startM = timestart[4:6]
    startD = timestart[6:8]

    for loca in locations[1:-1]:
        file = pathscn + "slr_"+secnario+"_"+source + loca + ".txt"
        data = pd.read_csv(file)
        data.columns = [loca]
        fdata = pd.concat([fdata, data], axis=1)

    pcps = []
    pcps.append(linespcp[0][0:-2])
    # print(pcps)
    datestart = startY + "-" + startM + "-" + startD
    time0 = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    timei = time0

    timein = []
    for i in fdata.index:
        Year = timei.year
        dateidlt = str(Year) + "-01-01"
        timeidlt = datetime.datetime.strptime(dateidlt, '%Y-%m-%d')
        dlt = (timei - timeidlt).days +1
        timei = timei + datetime.timedelta(days=1)
        txt = str(Year) + str(dlt).zfill(3)
        timein.append(txt)
    # print(timein)

    fdata1 = fdata.applymap(lambda x: f"%.3f" % x)
    fdata1 = fdata1.applymap(str)
    fdata1 = fdata1.applymap(lambda x: x.zfill(8))
    fdata1.insert(0, "timein", timein)
    fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
    tt = fdata1["contact"].to_list()
    pcps.extend(tt)
    pcpdf = pd.DataFrame(pcps)
    pcpdf.to_csv(pathSwat + "slr.slr", index=None, header=None)

def tranfWnd(pathdef,pathscn,pathSwat,secnario,source):
    print("TransF: sfcWind_",secnario,source)
    filepcp = pathdef + "pcp1.pcp"
    fpcp = open(filepcp, "r")
    linespcp = fpcp.readlines()
    spcp = linespcp[0]
    lstspcp = spcp.split(",")
    locations = []
    for lst in lstspcp:
        locations.append(lst[-14:])

    file = pathscn + "sfcWind_"+secnario+"_"+source + locations[0] + ".txt"
    fdata = pd.read_csv(file)
    timestart = fdata.columns[0]
    fdata.columns = [locations[0]]
    startY = timestart[:4]
    startM = timestart[4:6]
    startD = timestart[6:8]

    for loca in locations[1:-1]:
        file = pathscn + "sfcWind_"+secnario+"_"+source + loca + ".txt"
        data = pd.read_csv(file)
        data.columns = [loca]
        fdata = pd.concat([fdata, data], axis=1)

    pcps = []
    pcps.append(linespcp[0][0:-2])
    # print(pcps)
    datestart = startY + "-" + startM + "-" + startD
    time0 = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    timei = time0

    timein = []
    for i in fdata.index:
        Year = timei.year
        dateidlt = str(Year) + "-01-01"
        timeidlt = datetime.datetime.strptime(dateidlt, '%Y-%m-%d')
        dlt = (timei - timeidlt).days+1
        timei = timei + datetime.timedelta(days=1)
        txt = str(Year) + str(dlt).zfill(3)
        timein.append(txt)
    # print(timein)

    fdata1 = fdata.applymap(lambda x: f"%.3f" % x)
    fdata1 = fdata1.applymap(str)
    fdata1 = fdata1.applymap(lambda x: x.zfill(8))
    fdata1.insert(0, "timein", timein)
    fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
    tt = fdata1["contact"].to_list()
    pcps.extend(tt)
    pcpdf = pd.DataFrame(pcps)
    pcpdf.to_csv(pathSwat + "wnd.wnd", index=None, header=None)


if __name__== "__main__" :
    variables = ["pr", "tasmax", "tasmin", "sfcWind", "rsds", "hurs", "rlds"]
    scenarios = ["historical", "ssp126", "ssp245", "ssp370", "ssp585"]
    scenarios = ["ssp126", "ssp245", "ssp370", "ssp585"]

    sources = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'CanESM5',
               'CMCC-ESM2', 'EC-Earth3', 'EC-Earth3-Veg-LR',
               'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
               'MPI-ESM1-2-HR', 'MPI-ESM1-2-LR', 'MRI-ESM2-0',
               'NorESM2-LM', 'NorESM2-MM', "TaiESM1"]
    sources = ['CanESM5', 'CMCC-ESM2',
               'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0',
               'NorESM2-LM', 'NorESM2-MM', "TaiESM1"]


    pathdef = "G:/CMIP6/toTxtInOut01/WW/"
    pathSwat = "G:/CMIP6/toTxtInOut01/"
    pathscn = "G:/CMIP6/toSWATALL/"

    for scenario in scenarios:
        for source in sources:
            pathscn1 = pathscn + scenario + "/" +source +"/"
            pathSwat1 = pathSwat + scenario + "/" +source +"/"
            if not os.path.exists(pathSwat1):
                CIMP6_select.mkdir(pathSwat1)
            tranfPcp(pathdef,pathscn1,pathSwat1,scenario,source)
            tranfTmp(pathdef,pathscn1,pathSwat1,scenario,source)
            tranfHmd(pathdef,pathscn1,pathSwat1,scenario,source)
            tranfSlr(pathdef,pathscn1,pathSwat1,scenario,source)
            tranfWnd(pathdef,pathscn1,pathSwat1,scenario,source)