import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import PIL.ImageOps  
import cv2


directory = os.getcwd() + '\\S2_afterThresholdMask\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    loadSlope = Image.open("slopeFilter2.png").convert("1")
    # loadSlope = np.array(loadSlope)
    # loadSlope = np.invert(loadSlope)

    result = np.multiply(outputYear, loadSlope)
   
    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\S4_afterSlopeMask\\' + filename + '.png')


    
    