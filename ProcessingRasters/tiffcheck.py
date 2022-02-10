import os
import tifffile as tiff
import numpy as np
import slidingwindow as sw
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2
from osgeo import gdal

year = 2010
year_filename = year
sumyears = np.empty((6813, 3462))
yearslist = []

directory = os.getcwd() + '\\ImageYears\\'
pathlist = Path(directory).iterdir()

for path in pathlist:
  
    #outputYear = np.array(Image.open(str(path)))
    if year == 2012:
        year = year + 1
    
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    
    if filename == str(year):
        #loadimage = Image.open(str(path)).convert('1')
        loadimage = gdal.Open(str(path))
        outputYear = np.array(loadimage)
        # outputYear[np.isnan(outputYear)] = 0
        # outputYear[~np.isnan(outputYear)] = 1
        outputYear = Image.fromarray(outputYear).convert('1')
        outputYear.save(os.getcwd() + '\\binaryMasks\\' + year_filename + '_mask' + '.png')
        # sumyears = sumyears + outputYear
        # #yearslist.append(outputYear)
        # year = year + 1


#sum_output = np.concatenate(yearslist)
# sumyears = Image.fromarray(sumyears).convert('P')
# sumyears.save(os.getcwd() + '\\sumEachYear\\' + filename + '_sum' + '.png')
#print(sumyears.shape)








    
    # loadimage = Image.open(str(path)).convert('1')
    # loadimage.save(os.getcwd() + '\\binaryImages\\' + filename + '.png')


    

    
        
    # filepath = os.getcwd() + '\\LN_256\\' + filename + '.jpg'
    
    # tar_img = np.array(Image.open(str(filepath)))
    # tar_img = Image.fromarray(tar_img)

    # tar_img.save(os.getcwd() + '\\MS_LN_SET\\' + filename + '.png')