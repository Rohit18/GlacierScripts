import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2

#Apply CoBlanca filter on the images generated from Step2
directory = os.getcwd() + '\\onlyDebris_PP\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    loadFinalPP = Image.open("finalPP\\" + filename + ".png").convert("1")

    result = np.multiply(outputYear, loadFinalPP)
   
    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\Debris_PPTest\\' + filename + '.png')