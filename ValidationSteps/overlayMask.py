import os
import tifffile as tiff
import numpy as np
import slidingwindow as sw
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2

#for removing the NaNs from an no-rectangular rasters
#nanMaskImages = calculated from each Image year but might not be needed since same extent for each image
#results are stored in finalResults_*
#next, we should reference the images
#for referencing the images, I created another folder called toBeReferenced (needless) just to safeguard the data


directory = os.getcwd() + '\\binaryDebrisTemp\\'
# directory = os.getcwd() + '\\sumEachYear_Lakes\\'
pathlist = Path(directory).iterdir()

for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)    
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    maskPath = os.getcwd() + '\\nanMask24\\' + filename + '.png'
    loadMask = Image.open(str(maskPath)).convert('1') 
    loadMask = np.array(loadMask)

    result = np.multiply(outputYear, loadMask)
    # result = Image.fromarray(result).convert('L')
    result = Image.fromarray(result).convert('1')
    # result.save(os.getcwd() + '\\finalResults_LakesReverse\\' + filename + '.png')
    result.save(os.getcwd() + '\\binaryDebris\\' + filename + '.png')