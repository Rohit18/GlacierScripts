import os
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image
import cv2
import seaborn as sns

directory = os.getcwd() + '\\binaryDebris\\'
pathlist = Path(directory).iterdir()

variance = np.empty((6813, 3462))

images  = np.zeros((5, *variance.shape))

index = 0

filename_list = []

LS = []



for path in pathlist:


    while index < 25:
        #load predicted image
        loadimage = Image.open(str(path)).convert('1')
        outputYear = np.array(loadimage)
        print(index)
        images[index] = outputYear
        index = index + 6



    # #load target image
    # filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    # yearonfile = filename[0:4]    
    # filename = yearonfile
    # LS = Image.fromarray(outputYear)
    # LS.save(os.getcwd() + '\\binaryDebris\\' + filename + '.png')

sns.set()
ax = sns.heatmap(images.std(axis=0))
plt.show()