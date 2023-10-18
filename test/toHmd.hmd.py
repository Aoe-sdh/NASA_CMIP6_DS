import datetime
import time
import pandas as pd

pathSwat = "E:/CMIP6/CCTest/WW/"

pathscn = "E:/CMIP6/CCTest/ACCESS-CM2/"

filepcp = pathSwat + "pcp1.pcp"
fpcp = open(filepcp,"r")
linespcp = fpcp.readlines()
spcp = linespcp[0]
lstspcp = spcp.split(",")
locations = []
for lst in lstspcp:
    locations.append(lst[-14:])
# print(locations)

filetmp = pathSwat + "Tmp1.Tmp"
ftmp = open(filepcp,"r")
linestmp = fpcp.readlines()


file = pathscn + "hurs_historical_ACCESS-CM2"+locations[0] + ".txt"
fdata = pd.read_csv(file)
timestart = fdata.columns[0]
fdata.columns=[locations[0]]
timelen = len(fdata.index)
startY = timestart[:4]
startM = timestart[4:6]
startD = timestart[6:8]


df = pd.DataFrame
for loca in locations[1:-1]:
    file = pathscn + "hurs_historical_ACCESS-CM2" + loca + ".txt"
    data = pd.read_csv(file)
    data.columns=[loca]
    fdata = pd.concat([fdata,data],axis=1)

pcps = []
pcps.append(linespcp[0][0:-2])
print(pcps)
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


fdata1 = fdata.applymap(lambda x: f"%.3f" % x)
fdata1 = fdata1.applymap(str)
fdata1 = fdata1.applymap(lambda x:x.zfill(8))
fdata1.insert(0,"timein",timein)
fdata1["contact"] = fdata1.apply(lambda x: ''.join(x), axis=1)
tt = fdata1["contact"].to_list()
pcps.extend(tt)
pcpdf = pd.DataFrame(pcps)
pcpdf.to_csv(pathSwat + "hmd.pcp",index=None,header=None)