import os
import numpy as np
from pathlib import Path
from PIL import Image

#Apply CoBlanca filter on the images generated from Step2
directory = os.getcwd() + '\\S15_afterSumThreshold\\'
pathlist = Path(directory).iterdir()


for path in pathlist:

    loadimage = Image.open(str(path))
    outputYear = np.array(loadimage)

    filename = str(os.path.basename(path))[:str(os.path.basename(path)).find(".")]
    filename = filename[0:4]

    noiseMask = os.getcwd() + '\\S17A_NoiseMasks\\' + filename + '.png'
    noiseMask = Image.open(str(noiseMask))
    noiseMask = np.array(noiseMask)

    result = np.multiply(outputYear, noiseMask)
   
    result = Image.fromarray(result)
    result.save(os.getcwd() + '\\S17B_applyNoiseMasks\\' + filename + '.png')