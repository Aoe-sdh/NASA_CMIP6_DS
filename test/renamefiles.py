import os

inpath = "C:/zxDownscale/LAI250/"
outpath = "C:/zxDownscale/LAI250Rename/"
filenames = os.listdir(inpath)
print(filenames)
for filename in filenames:
    v1 = filename[:11]
    v2 = filename[11:15]
    v3 = filename[15:24]
    v4 = filename[24:30]
    v5 = filename[30:]
    name = inpath + filename
    newname = outpath + "MOD13Q1." + v3 + v4 + ".060." + "2022101860549.hdf"
    print(v1,v2,v3,v4,v5)
    print(newname)
    os.rename(name,newname)
