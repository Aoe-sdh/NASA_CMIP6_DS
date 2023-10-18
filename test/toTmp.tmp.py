import datetime
import time
import pandas as pd

pathSwat = "E:/CMIP6/CCTest/WW/"

pathscn = "E:/CMIP6/CCTest/ACCESS-CM2/"

filetmp = pathSwat + "pcp1.pcp"
ftmp = open(filetmp,"r")
linestmp = ftmp.readlines()
stmp = linestmp[0]
lststmp = stmp.split(",")
locations = []
for lst in lststmp:
    locations.append(lst[-14:])
# print(locations)

file = pathscn + "ta_historical_ACCESS-CM2"+locations[0] + ".txt"
fdata0 = pd.read_csv(file)
timestart = fdata0.columns[0]
timelen = len(fdata0.index)
startY = timestart[:4]
startM = timestart[4:6]
startD = timestart[6:8]

file = pathscn + "ta_historical_ACCESS-CM2"+locations[0] + ".txt"
fdata = pd.read_csv(file,skiprows=1,names=[locations[0]+"min",locations[0]+"max"])

df = pd.DataFrame
for loca in locations[1:-1]:
    file = pathscn + "ta_historical_ACCESS-CM2" + loca + ".txt"
    data = pd.read_csv(file,skiprows=1,names=[loca+"min",loca+"max"])
    # print(data)
    # # data.columns=
    # time.sleep(1000)
    fdata = pd.concat([fdata,data],axis=1)

tmps = []
tmps.append(linestmp[0][0:-2])
tmps.append(linestmp[1][0:-2])
tmps.append(linestmp[2][0:-2])
tmps.append(linestmp[3][0:-2])
print(tmps)
datestart = startY + "-" +startM + "-" + startD
time0 = datetime.datetime.strptime(datestart,'%Y-%m-%d')
timei = time0

timein = []
for i in fdata.index:
    Year = timei.year
    dateidlt = str(Year)+"-01-01"
    timeidlt = datetime.datetime.strptime(dateidlt,'%Y-%m-%d')
    dlt = (timei-timeidlt).days
    timei = timei + datetime.timedelta(days=1)
    txt = str(Year)+str(dlt).zfill(3)
    timein.append(txt)
print(timein)


fdata1 = fdata.apply(lambda x: round(x,1), axis=1)
fdata1 = fdata1.applymap(str)
fdata1 = fdata1.applymap(lambda x:x.zfill(5))
fdata1.insert(0,"timein",timein)
fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
tt = fdata1["contact"].to_list()
tmps.extend(tt)
pcpdf = pd.DataFrame(tmps)
pcpdf.to_csv(pathSwat + "tmp.tmp",index=None,header=None)