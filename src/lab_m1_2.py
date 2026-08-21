import numpy as np
import cv2 as cv

# helper methods
def open_image(img_path):
    img = cv.imread(img_path,cv.IMREAD_UNCHANGED)
    assert img is not None, "file could not be read, check with os.path.exists()"
    return img

# methods lab-m1.2
# brightness
def brightness(img_path, output_path, value, *args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg = tempImg.astype(np.int16)

    try:
        brightness = int(value)
    except ValueError:
        raise ValueError("Value (-v) must be an integer")
    if brightness not in range(-256, 256):
        raise ValueError("Value (-v) must be in the range (-255, 255)")

    tempImg[..., :3] = np.clip(tempImg[..., :3] + brightness,0,255)

    tempImg = tempImg.astype(np.uint8)
    cv.imwrite(output_path, tempImg)

# contrast
def contrast(img_path, output_path, value, *args):
    img = open_image(img_path)
    tempImg = np.copy(img)
    tempImg = tempImg.astype(np.int16)

    try:
        alpha = float(value)
    except ValueError:
        raise ValueError("Value (-v) must be a float")
    if not 0.0 <= alpha <= 10.0:
        raise ValueError("Value (-v) must be in the range (0.0, 10.0)")

    tempImg[..., :3] = np.clip(alpha * (tempImg[..., :3] - 128) + 128,0,255)

    tempImg = tempImg.astype(np.uint8)
    cv.imwrite(output_path, tempImg)
# negative
# threshold
# histogram

operations = {
        'brightness': brightness,
        'contrast': contrast
    }