import os
from osgeo import gdal
import numpy as np
from scipy.signal import savgol_filter


# 读取tif数据集
def readTif(fileName):
    dataset = gdal.Open(fileName)
    if dataset == None:
        print(fileName + "文件无法打开")
    return dataset


# 保存tif文件函数
def writeTiff(im_data, im_geotrans, im_proj, path):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32
    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    elif len(im_data.shape) == 2:
        im_data = np.array([im_data])
        im_bands, im_height, im_width = im_data.shape
    # 创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(path, int(im_width), int(im_height), int(im_bands), datatype)
    if (dataset != None):
        dataset.SetGeoTransform(im_geotrans)  # 写入仿射变换参数
        dataset.SetProjection(im_proj)  # 写入投影
    for i in range(im_bands):
        dataset.GetRasterBand(i + 1).WriteArray(im_data[i])
    del dataset


def SG_filter(tifFolder, suffix):
    '''
    tifFolder tif所在文件夹
    suffix 生成结果文件名后缀
    '''
    #  获取文件夹内的文件名
    tifNameList = os.listdir(tifFolder)
    tifPath = tifFolder + "/" + tifNameList[0]
    dataset = readTif(tifPath)
    width = dataset.RasterXSize  # 栅格矩阵的列数
    height = dataset.RasterYSize  # 栅格矩阵的行数
    Tif_geotrans = dataset.GetGeoTransform()
    Tif_proj = dataset.GetProjection()
    Tif_data = dataset.ReadAsArray(0, 0, width, height)  # 获取数据
    Tif_datas = np.zeros((len(tifNameList), Tif_data.shape[0], Tif_data.shape[1]))
    for i in range(len(tifNameList)):
        tifPath = tifFolder + "/" + tifNameList[i]
        dataset = readTif(tifPath)
        Tif_data = dataset.ReadAsArray(0, 0, width, height)  # 获取数据
        Tif_datas[i] = Tif_data
    #  维度切换，便于后面的提取每个像素对应的各个时期值
    Tif_datas = Tif_datas.swapaxes(1, 0)
    Tif_datas = Tif_datas.swapaxes(1, 2)

    SGfilter = np.zeros(Tif_datas.shape)
    for i in range(Tif_datas.shape[0]):
        for j in range(Tif_datas.shape[1]):
            SGfilter[i][j] = savgol_filter(Tif_datas[i][j], window_length=7, polyorder=2)
            #  维度切换回去
    SGfilter = SGfilter.swapaxes(1, 0)
    SGfilter = SGfilter.swapaxes(0, 2)

    for i in range(SGfilter.shape[0]):
        SavePath = os.path.splitext(tifNameList[i])[0] + suffix + ".tif"
        writeTiff(SGfilter[i], Tif_geotrans, Tif_proj, SavePath)


SG_filter(r"F:\MODISNDVI\HJNDVI60_250s", "_LSTSGfilter")