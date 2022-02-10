import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2


#folder where the images are
directory = os.getcwd() + '\\S4_afterCoBlanca\\'
pathlist = Path(directory).iterdir()

#go through each image
for path in pathlist:

    #load each image
    loadimage = Image.open(str(path))

    #convert to numpy array
    outputYear = np.array(loadimage)    
    
    #extract filename
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    #only select top pixel which are higher than 1
    icePixels = outputYear > 1

    result = np.multiply(outputYear, icePixels)

    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\S6_deletePixels\\' + filename + '.png')
