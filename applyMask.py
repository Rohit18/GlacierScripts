import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2
from sklearn.preprocessing import binarize

#Apply CoBlanca filter on the images generated from Step2
directory = os.getcwd() + '\\S6_afterSumThreshold\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadfilter1 = Image.open(str(path)).convert('L')
    loadfilter1 = np.array(loadfilter1)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    # loadCoBlanca = Image.open("filterFiles\\RGI_Cordillera_Blanca_2000m_LAKE_buffer_binary_resampled.tif").convert("1")
    loadfilter2 = Image.open( os.getcwd() + "\\S6_afterSlope\\" + filename + ".png").convert('L')
    loadfilter2 = np.array(loadfilter2)

    filter1 = binarize(loadfilter1) 
    filter2 = binarize(loadfilter2) 

    filter = np.multiply(filter1, filter2)

    # result = Image.fromarray(filter)    
    # result.save(os.getcwd() + '\\S4\\' + filename + '.png')

    originalImage = Image.open(os.getcwd() + "\\S4_afterSumThreshold\\" + filename + ".png")

    # loadSlope = np.invert(loadSlope)
    
    result = np.multiply(originalImage, filter)


    # result = np.multiply(outputYear, loadCoBlanca)
    # result = np.add(outputYear, loadCoBlanca)

    # print(result.max())
    # print(filename)
    # print("max")

    # deletePixels = result > 1
    # result = np.multiply(outputYear, deletePixels)

    # print(result.min())
    # print(filename)
    # print("min should be 0")

    # # result = result - 1

    # # print(result.min())
    # # print(result.min())
    # # print(filename)
    # # print("subtract 1")

    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\S7\\' + filename + '.png')