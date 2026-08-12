import numpy as np
import cv2 as cv

img = cv.imread('donkey.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

width,height,channels = img.shape
print("width: ", width ,"\nheight: ", height ,"\nchannels: ", channels ,"\npixels: ", img.size, "\ntype: ", img.dtype)