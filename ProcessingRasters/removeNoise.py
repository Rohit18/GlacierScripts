import os

import numpy as np
from pathlib import Path
from PIL import Image
import cv2

#Apply CoBlanca filter on the images generated from Step2
directory = os.getcwd() + '\\S2_afterDEM_Glacier\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    loadCoBlanca = Image.open("filterFiles\\CoBlanca.tif").convert('1')

    result = np.multiply(outputYear, loadCoBlanca)
   
    result = Image.fromarray(result).convert('1')
    result.save(os.getcwd() + '\\S4_afterCoBlanca\\' + filename + '.png')