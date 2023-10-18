from osgeo import gdal,ogr

import os

inputpath = "F:/MODISNDVI/test/hmd_ave_Krige_Annual_Project11.tif"
outputpath = "F:/MODISNDVI/test/hmd_ave_Krige_Annual_Project11_Cut.tif"
shp = "C:/zxDownscale/HJ0001kmBuffer.shp"


dataset1 = gdal.Open(inputpath)
gdal.Warp(outputpath,dataset1,cutlineDSName=shp,cropToCutline = True,dstNodata = 0)