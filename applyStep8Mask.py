import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2

#change directory
directory = os.getcwd() + '\\S6B_afterZoneMask\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    maskPath = os.getcwd() + '\\S8B_afterRGIThresholdStep8_Glacier\\' + filename + '.png'
    loadMask = Image.open(str(maskPath)).convert('1') 
    loadMask = np.array(loadMask)

    result = np.multiply(outputYear, loadMask)
   
    result = Image.fromarray(result).convert('L')
    result.save(os.getcwd() + '\\S8C_afterStep8Mask\\' + filename + '.png')