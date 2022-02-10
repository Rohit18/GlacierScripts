import os
import numpy as np
from pathlib import Path
from PIL import Image
import sys

#To calculate Glacier+Debris and just Glacier: expected to decrease in the future

# year_filename = sys.argv[1]
# year = int(year_filename)
sumyears = np.empty((6813, 3462))

directory = os.getcwd() + '\\glacier_binary_renamed\\'
pathlist = Path(directory).iterdir()

listoffiles = []

for path in pathlist:
    
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]    

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)
    sumyears = sumyears + outputYear
    
sumImages = Image.fromarray(sumyears).convert('L') #'L' since the image is binary no more
sumImages.save(os.getcwd() + '\\glacier_summation\\test.png')