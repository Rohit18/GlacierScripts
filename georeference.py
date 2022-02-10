from osgeo import gdal, ogr, osr
import os
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Variables:
#referencedImages - extract references
#unreferencedPth - to be referenced
#target_path - new folder to store the newly referenced images

foldertoreference = sys.argv[1]
newfolder = str(foldertoreference) + '_ref'

directory = os.getcwd() + '\\referencedImages\\'
pathlist = Path(directory).iterdir()

for path in pathlist:

    #driver = ogr.GetDriverByName('GTiff')
    ds = gdal.Open(str(path))
    gt = ds.GetGeoTransform()
    proj = ds.GetProjection()
    ref_filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    ref_filename = ref_filename[0:4]

    unreferenced_path = os.getcwd() + '\\' + foldertoreference + '\\' + ref_filename + '.png'
    unreferenced_image = Image.open(str(unreferenced_path))
    unreferenced_array = np.array(unreferenced_image)

    if not os.path.exists(os.getcwd() + '\\' + newfolder + '\\'):
        os.makedirs(os.getcwd() + '\\' + newfolder + '\\')

    # target_path = os.getcwd() + '\\' + newfolder + '\\'+ ref_filename + '.tif'
    
    ##Final Step Raster Save Name
    target_path = os.getcwd() + '\\' + newfolder + '\\'+ 'PP_lower_lakes_' + ref_filename + 'summed.tif'

    driver = gdal.GetDriverByName("GTiff")
    driver.Register()
    outds = driver.Create(target_path, xsize = unreferenced_array.shape[1], ysize = unreferenced_array.shape[0], eType = gdal.GDT_Byte)
    outds.SetGeoTransform(gt)
    outds.SetProjection(proj)
    outband = outds.GetRasterBand(1)
    outband.WriteArray(unreferenced_array)
