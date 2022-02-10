import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2

#Apply CoBlanca filter on the images generated from Step2
directory = os.getcwd() + '\\PixelValue1\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[4:8]

    loadCoBlanca = Image.open("filterFiles\\CoBlanca.tif")

    result = np.multiply(outputYear, loadCoBlanca)
   
    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\Filter_Step8\\' + filename + '.png')