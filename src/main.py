import argparse
import os
import numpy as np
import cv2 as cv
from pathlib import Path
from datetime import datetime

# global vars
img_default_path = Path(__file__).parent.parent/'images'

# helper methods
def open_image(img_path):
    img = cv.imread(img_path)
    assert img is not None, "file could not be read, check with os.path.exists()"
    return img

# methods lab-m1.1
# inspect
def inspect(img_path):
    img = open_image(img_path)
    width,height,channels = img.shape
    print(f'width: {width}\nheight: {height}\nchannels: {channels}\npixels: {img.size}\ntype: {img.dtype}')
    for i in range(channels):
        print(f'channel {i} min: {np.min(img[:,:,i])} max: {np.max(img[:,:,i])} mean: {np.mean(img[:,:,i]):.3f}')

# copy
def copy(img_path, output_path):
    img = open_image(img_path)
    tempImg = np.copy(img)
    cv.imwrite(output_path, tempImg)

# channel_b
def channel_b(img_path, output_path):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg[:,:,1:3] = 0
    cv.imwrite(output_path, tempImg)

# channel_g
def channel_g(img_path, output_path):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg[:,:,0] = 0
    tempImg[:,:,2] = 0
    cv.imwrite(output_path, tempImg)

# channel_r
def channel_r(img_path, output_path):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg[:,:,0:2] = 0
    cv.imwrite(output_path, tempImg)

# grayscale_average
def grayscale_average(img_path, output_path):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg = np.mean(tempImg, axis=2).astype(np.uint8)
    cv.imwrite(output_path, tempImg)

# grayscale_weighted
def grayscale_weighted(img_path, output_path):
    img = open_image(img_path)
    weights = np.array([0.299, 0.587, 0.114])

    tempImg = np.copy(img)
    tempImg = np.dot(tempImg[...,:3], weights).astype(np.uint8)
    cv.imwrite(output_path, tempImg)

# quantize


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='arguments for pdi_lab')

    parser.add_argument('-i', '--input', type=str,default=os.path.join(img_default_path, 'input', 'donkey.jpg'), help='input path+file')
    parser.add_argument('-o', '--output', type=str,default=os.path.join(img_default_path, 'output', datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'), help='output path+file')
    parser.add_argument('-p', '--operation', type=str,required=True, help='operation to perform',
                        choices=['inspect', 
                                 'copy', 
                                 'channel_b', 
                                 'channel_g', 
                                 'channel_r', 
                                 'grayscale_average', 
                                 'grayscale_weighted'])
    #parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    args = parser.parse_args()

    if args.operation == 'inspect':
        inspect(args.input)
    elif args.operation == 'copy':
        copy(args.input, args.output)
    elif args.operation == 'channel_b':
        channel_b(args.input, args.output)
    elif args.operation == 'channel_g':
        channel_g(args.input, args.output)
    elif args.operation == 'channel_r':
        channel_r(args.input, args.output)
    elif args.operation == 'grayscale_average':
        grayscale_average(args.input, args.output)
    elif args.operation == 'grayscale_weighted':
        grayscale_weighted(args.input, args.output)