import numpy as np
import cv2 as cv

img = cv.imread('shrek3.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

width,height,channels = img.shape
print("width: ", width ,"\nheight: ", height ,"\nchannels: ", channels ,"\npixels: ", img.size, "\ntype: ", img.dtype)

img[:,:,1:3] = 0
wtv = img[0,0,2]
print("\n algo:", wtv)
cv.imshow('a',img)
cv.waitKey()