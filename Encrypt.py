import cv2
import numpy as np
from FY_Algorithm import *
from Gen_Seq import *


def Encrypt(image):
    h, w = image.shape
    image = image.flatten()

    scramble_seq = Gen_Float_Seq(image.size)
    scramble_img, order = diffusion(image, scramble_seq)
    permutation_seq = Gen_Int_Seq(image.size, 256)

    for i in range(image.size):
        scramble_img[i] ^= permutation_seq[i]

    return scramble_img.reshape([h, w]), order


if __name__ == '__main__':
    image = cv2.imread("Images/Lena.bmp")[:, :, 0]
    image, order = Encrypt(image)
    print(image)
