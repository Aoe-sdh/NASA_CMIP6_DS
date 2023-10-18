from osgeo import gdal,ogr

import os

inputpath = "F:/MODISNDVI/MODVIS_NDVI60_250m_H27V05VItif/"
outputpath = "F:/MODISNDVI/HJNDVI60_250VI/"
shp = "C:/zxDownscale/HJ0001kmBuffer.shp"

filenames = os.listdir(inputpath)
for file in filenames:
    print(file)
    inputtif = inputpath + file
    outputtif = outputpath + "HJ_" +file
    dataset1 = gdal.Open(inputtif)
    gdal.Warp(outputtif,dataset1,cutlineDSName=shp,cropToCutline = True,dstNodata = 0)