import cv2, os
import numpy as np


for image in os.listdir("Y_images"):
    Y_channel = cv2.imread("Y_images/" + image)[:, :, 0]
    Cb_channel = cv2.imread("decompressed/Cb_decompressed/" + image)[:, :, 0]
    Cr_channel = cv2.imread("decompressed/Cr_decompressed/" + image)[:, :, 0]
    reconstruct_image = cv2.imread("YCbCr_images/" + image)

    reconstruct_image[:, :, 0] = Y_channel
    reconstruct_image[:, :, 1] = Cb_channel
    reconstruct_image[:, :, 2] = Cr_channel

    RGB = cv2.cvtColor(reconstruct_image, cv2.COLOR_YCR_CB2BGR)
    cv2.imwrite("reconstruction_images/{}".format(image), RGB)
