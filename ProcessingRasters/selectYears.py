import os
import tifffile as tiff
import numpy as np
import slidingwindow as sw
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2

# year = 2010
# year_filename = year
sumyears = np.empty((6813, 3462))
yearslist = []

directory = os.getcwd() + '\\binaryLakes\\'
pathlist = Path(directory).iterdir()

for year in range(2020, 1986, -1):

    year_filename = str(year)
    if year == 2012:
            continue

    for path in pathlist:
        print(year)
    
        #outputYear = np.array(Image.open(str(path)))
        if year == 2012:
            year = year - 1
        
        filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
        
        if filename == str(year):
            loadimage = Image.open(str(path)).convert('1')
            outputYear = np.array(loadimage)
            sumyears = sumyears + outputYear
            #yearslist.append(outputYear)
            year = year - 1

    print(sumyears.max())
    sumImages = Image.fromarray(sumyears).convert('L')
    sumImages.save(os.getcwd() + '\\sumEachYear_Lakes\\' + year_filename + '_sum' + '.png')
    
    sumyears = np.empty((6813, 3462))
    outputYear = np.empty((6813, 3462))









    
    # loadimage = Image.open(str(path)).convert('1')
    # loadimage.save(os.getcwd() + '\\binaryImages\\' + filename + '.png')


    

    
        
    # filepath = os.getcwd() + '\\LN_256\\' + filename + '.jpg'
    
    # tar_img = np.array(Image.open(str(filepath)))
    # tar_img = Image.fromarray(tar_img)

    # tar_img.save(os.getcwd() + '\\MS_LN_SET\\' + filename + '.png')