import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2

# add arguments, example text filename "example.txt"
countFileName = sys.argv[1]

#folder where the images are
directory = os.getcwd() + '\\S10B_applyNoiseMasks\\'
pathlist = Path(directory).iterdir()

#create textfile in write mode
file1 = open(countFileName,"w")

#go through each image
for path in pathlist:

    #load each image
    loadimage = Image.open(str(path))

    #convert to numpy array
    outputYear = np.array(loadimage)    
    
    #extract filename
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]
    
    #determine max pixel value for each
    # maxVal = outputYear.max()

    #define the minimum value, 0.35 removes the bottom 65%
    # minVal = int(maxVal - 0.35 * maxVal)

    #only select the top pixels
    # icePixels = [outputYear >= minVal]

    #only select the top pixels
    # icePixels = [outputYear == maxVal]

    #count each non zero pixel
    count = np.count_nonzero(outputYear)

    #write on file, this will print the count for each year output per line
    file1.writelines(str(count))
    file1.writelines("\n")

#close text file
file1.close()