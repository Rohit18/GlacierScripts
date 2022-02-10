import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2

#Apply CoBlanca filter on the images generated from Step2
directory = os.getcwd() + '\\S4\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    # loadCoBlanca = Image.open("filterFiles\\RGI_Cordillera_Blanca_2000m_LAKE_buffer_binary_resampled.tif").convert("1")
    # loadCoBlanca = Image.open("filterFiles\\CoBlanca_Buffer.png")
    loadDEM = Image.open("filterFiles\\DEM_5050.png")

    # loadCoBlanca = np.invert(loadCoBlanca)
    loadDEM = np.invert(loadDEM)

    result = np.multiply(outputYear, loadDEM)


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
    result.save(os.getcwd() + '\\S5A_afterDEM5050\\' + filename + '.png')