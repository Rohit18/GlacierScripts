import os
import tifffile as tiff
import numpy as np
import slidingwindow as sw
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2

#This is for only dealing and calculating the pixels with the max pixel values in each summed Image per year
#Now we are extracting ranges, so might not need it
#there is code for extracting the top 10% of the pixel values

directory = os.getcwd() + '\\finalResults_Lakes\\'
pathlist = Path(directory).iterdir()

for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)    
    # filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    # filename = filename[0:4]
    
    maxVal = outputYear.max()
    #minVal = int(maxVal - 0.2 * maxVal)

    icePixels = [outputYear == maxVal]

    # maxPixels = outputYear == (outputYear.max() - 1)
    # count = np.count_nonzero(maxPixels)

    count = np.count_nonzero(icePixels)

    print(count)
