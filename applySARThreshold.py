import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image
import cv2


directory = os.getcwd() + '\\S4A_afterSumThreshold_Glacier\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    loadSAR = Image.open("filterFiles\\sarFilter3.png").convert("1")

    result = np.multiply(outputYear, loadSAR)
   
    result = Image.fromarray(result).convert('1')
    result.save(os.getcwd() + '\\S8A_afterSARThreshold_Glacier\\' + filename + '.png')


    
    