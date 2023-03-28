import cv2, time
import numpy as np


def image_to_digits(image):
    if len(image.shape) == 2:
        h, w = image.shape
        c = 1
    else:
        h, w, c = image.shape

    c *= 8

    digits_array = np.unpackbits(image)
    # return digits_array
    return digits_array.reshape([h, w, c])


def digits_to_image(digits_array, shape):
    return np.packbits(digits_array).reshape(shape)

