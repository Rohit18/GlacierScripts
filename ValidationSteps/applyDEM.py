import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2


directory = os.getcwd() + '\\sumDebris\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    loadDEM = Image.open("filterFiles\\demFilter_4100.png").convert("1")

    result = np.multiply(outputYear, loadDEM)
   
    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\S2_afterDEM\\' + filename + '.png')


    
    