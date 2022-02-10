import sys
import os
from pathlib import Path
import numpy as np
from PIL import Image
from natsort import natsorted

#Calculating Lakes and Debris: Expected to increase through years


year_filename = sys.argv[1]
year = int(year_filename)
sumyears = np.empty((6813, 3462))

directory = os.getcwd() + '\\DebrisBinary\\'
pathlist = Path(directory).iterdir()
listoffiles = []

for path in pathlist:
    listoffiles.append(path)

for filepath in reversed(listoffiles):
    #skip 2012 since incomplete data
    if year == 1993:
        year = year - 1

    if year == 2012:
        year = year - 1

    
    filename = str(os.path.basename(filepath))[:str(os.path.basename(filepath)).find(".")]
    
    if filename == str(year):
        loadimage = Image.open(str(filepath))
        outputYear = np.array(loadimage)
        sumyears = sumyears + outputYear
        year = year - 1


sumImages = Image.fromarray(sumyears).convert('L') #'L' since the image is binary no more
sumImages.save(os.getcwd() + '\\sumDebris_PP\\' + year_filename + '_sum' + '.png')
