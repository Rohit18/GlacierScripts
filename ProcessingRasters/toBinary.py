import os
import tifffile as tiff
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2

directory = os.getcwd() + '\\Debris_PNG\\'
pathlist = Path(directory).iterdir()

filename_list = []

LS = []

for path in pathlist:

    #load predicted image
    # loadimage = Image.open(str(path))
    img_grey = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)

    # thresh = 1
    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    img_binary = cv2.threshold(img_grey, 1, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite(os.getcwd() + '\\DebrisBinary\\' + filename + '.png',img_binary) 

    # outputYear = np.array(img_grey)
    # #N = np.array(Image.open(str(path)))
    # #N = N[:,:,1]
    
    # #load target image
    # filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    # # yearonfile = filename[1:5]    
    # # filename = yearonfile
    # LS = Image.fromarray(outputYear).convert("L")
    # LS.save(os.getcwd() + '\\DebrisBinary\\' + filename + '.png')
    # print(filename)




