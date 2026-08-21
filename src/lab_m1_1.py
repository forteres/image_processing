import numpy as np
import cv2 as cv

# helper methods
def open_image(img_path):
    img = cv.imread(img_path)
    assert img is not None, "file could not be read, check with os.path.exists()"
    return img

# methods lab-m1.1
# inspect
def inspect(img_path,*args):
    img = open_image(img_path)
    width,height,channels = img.shape
    print(f'width: {width}\nheight: {height}\nchannels: {channels}\npixels: {img.size}\ntype: {img.dtype}')
    for i in range(channels):
        print(f'channel {i} min: {np.min(img[:,:,i])} max: {np.max(img[:,:,i])} mean: {np.mean(img[:,:,i]):.3f}')

# copy
def copy(img_path, output_path,*args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    cv.imwrite(output_path, tempImg)

# channel_b
def channel_b(img_path, output_path,*args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg[:,:,1:3] = 0
    cv.imwrite(output_path, tempImg)

# channel_g
def channel_g(img_path, output_path,*args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg[:,:,0] = 0
    tempImg[:,:,2] = 0
    cv.imwrite(output_path, tempImg)

# channel_r
def channel_r(img_path, output_path,*args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg[:,:,0:2] = 0
    cv.imwrite(output_path, tempImg)

# grayscale_average
def grayscale_average(img_path, output_path,*args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg = np.mean(tempImg, axis=2).astype(np.uint8)
    cv.imwrite(output_path, tempImg)

# grayscale_weighted
def grayscale_weighted(img_path, output_path,*args):
    img = open_image(img_path)
    weights = np.array([0.299, 0.587, 0.114])

    tempImg = np.copy(img)
    tempImg = np.dot(tempImg[...,:3], weights).astype(np.uint8)
    cv.imwrite(output_path, tempImg)

# quantize
def quantize(img_path, output_path, value):
    img = open_image(img_path)
    tempImg = np.copy(img)

    try:
        levels = int(value)
    except ValueError:
        raise ValueError("Value (-v) must be an integer")

    if levels not in (2, 4, 8, 16):
        raise ValueError("Value (-v) must be in (2, 4, 8, 16)")
    
    factor = 255 / (levels - 1)
    tempImg = np.round(tempImg / factor) * factor
    tempImg = tempImg.astype(np.uint8)
    cv.imwrite(output_path, tempImg)

operations = {
        'inspect': inspect,
        'copy': copy,
        'channel_b': channel_b,
        'channel_g': channel_g,
        'channel_r': channel_r,
        'grayscale_average': grayscale_average,
        'grayscale_weighted': grayscale_weighted,
        'quantize': quantize
    }