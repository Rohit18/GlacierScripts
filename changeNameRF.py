import os
import tifffile as tiff
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2

directory = os.getcwd() + '\\onlyDebris\\'
pathlist = Path(directory).iterdir()

filename_list = []

LS = []

for path in pathlist:

    #load predicted image
    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)
    #N = np.array(Image.open(str(path)))
    #N = N[:,:,1]
    
    #load target image
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    yearonfile = filename[1:5]    
    filename = yearonfile
    LS = Image.fromarray(outputYear)
    LS.save(os.getcwd() + '\\onlyDebris_PP\\' + filename + '.png')
    # print(filename)




