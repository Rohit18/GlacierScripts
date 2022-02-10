import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2
# from skimage.util import img_as_ubyte


imageFolder = str(sys.argv[1])
thresholdVal = float(sys.argv[2])



#folder where the images are
directory = os.getcwd() + '\\' + imageFolder + '\\'
pathlist = Path(directory).iterdir()

#go through each image
for path in pathlist:

    #load each image
    loadimage = Image.open(str(path))

    #convert to numpy array
    outputYear = np.array(loadimage)
    icePixels = outputYear 
    
    #extract filename
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]
    
    #determine max pixel value for each
    maxVal = outputYear.max()

    #define the minimum value, 0.35 removes the bottom 65%
    minVal = int(maxVal - thresholdVal * maxVal)
    # print(minVal)

    result = np.where(outputYear > minVal, 255, 0)
    # binary_where = img_as_ubyte(binary_where)

    # print(minVal)
    # result = outputYear[np.where(outputYear<=minVal)]
    # result = (lower < outputYear) & (img < upper)
    # result = np.array(1.0 * (outputYear < minVal))

    #only select the top pixels
    #icePixels = icePixels[outputYear < minVal])


    result = Image.fromarray(result).convert('1')

    mainImage = os.getcwd() + '\\' + imageFolder + '\\' + filename + '.png'
    mainImage = Image.open(str(mainImage))
    mainImage = np.array(mainImage)

    applyMask = np.multiply(mainImage, result)
    applyMask = Image.fromarray(applyMask)

    applyMask.save(os.getcwd() + '\\S6_afterSumThreshold\\' + filename + '.png')