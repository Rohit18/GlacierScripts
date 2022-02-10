import os
import tifffile as tiff
import numpy as np
import slidingwindow as sw
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2

year = 2019
year_filename = str(year)
sumyears = np.empty((6813, 3462))

directory = os.getcwd() + '\\binaryLakes\\'
pathlist = Path(directory).iterdir()
listoffiles = []

for path in pathlist:
    listoffiles.append(path)

for filepath in reversed(listoffiles):
    #skip 2012 since incomplete data
    if year == 2012:
        year = year - 1
    
    filename = str(os.path.basename(filepath))[:str(os.path.basename(filepath)).find(".")]
    
    if filename == str(year):
        loadimage = Image.open(str(filepath)).convert('1')
        outputYear = np.array(loadimage)
        sumyears = sumyears + outputYear
        year = year - 1


sumImages = Image.fromarray(sumyears).convert('L') #'L' since the image is binary no more
sumImages.save(os.getcwd() + '\\sumEachYear_Lakes\\' + year_filename + '_sum' + '.png')
