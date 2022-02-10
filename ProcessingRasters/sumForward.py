import os
import numpy as np
from pathlib import Path
from PIL import Image
import sys

#To calculate Glacier+Debris and just Glacier: expected to decrease in the future

year_filename = sys.argv[1]
year = int(year_filename)
sumyears = np.empty((6813, 3462))

directory = os.getcwd() + '\\glacier_binary_renamed\\'
pathlist = Path(directory).iterdir()

listoffiles = []

for path in pathlist:
    listoffiles.append(str(path))

listoffiles.sort()

for path in listoffiles:

    # print(path)

    if year == 1993:
        year = year + 1

    if year == 2012:
        year = year + 1
    
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    # print(filename)
    #filename = filename[7:11]   
    
    if filename == str(year):
        loadimage = Image.open(str(path))
        outputYear = np.array(loadimage)
        sumyears = sumyears + outputYear
        year = year + 1
        # count = np.count_nonzero(sumyears)
        # print(count)
    
sumImages = Image.fromarray(sumyears).convert('L') #'L' since the image is binary no more
sumImages.save(os.getcwd() + '\\glacier_summation\\' + year_filename + '.png')