import argparse
import numpy as np
import cv2 as cv
from pathlib import Path
from datetime import datetime

img = cv.imread(Path(__file__).parent.parent/'images/input/donkey.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

width,height,channels = img.shape
print("width: ", width ,"\nheight: ", height ,"\nchannels: ", channels ,"\npixels: ", img.size, "\ntype: ", img.dtype)

img[:,:,1:3] = 0
wtv = img[0,0,2]
print("\n algo:", wtv)
cv.imshow('a',img)
cv.waitKey()

#methods lab-m1.1
# inspect
# copy
# channel_b
# channel_g
# channel_r
# grayscale_average
# grayscale_weighted
# quantize


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='arguments for pdi_lab')

    parser.add_argument('-i', '--input', type=str,default=Path(__file__).parent.parent/'images/input/donkey.jpg', help='input path+file')
    parser.add_argument('-o', '--output', type=str,default=Path(__file__).parent.parent/'images/output/%s.jpg' % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), help='output path+file')
    parser.add_argument('-p', '--operation', type=str,required=True, help='operation to perform')
    #parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    args = parser.parse_args()