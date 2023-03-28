import numpy as np
import os
import cv2
from skimage.metrics import structural_similarity

sum = 0
length = 0
max = -9999
min = 99999


def SSIM(cover, stego):
    b1, g1, r1 = cv2.split(cover)
    b2, g2, r2 = cv2.split(stego)

    score1, a1 = structural_similarity(b1, b2, full=True)
    score2, a2 = structural_similarity(g1, g2, full=True)
    score3, a3 = structural_similarity(r1, r2, full=True)
    return (score1 + score2 + score3) / 3


def PSNR(img1, img2):
    diff = img1 - img2
    MSE = (diff ** 2).mean(axis=None)
    if not MSE:
        return 0, "inf", 1.0

    psnr = 10 * np.log10(255 * 255 / MSE)
    return psnr


def main():
    global min
    for index, image in enumerate(os.listdir("kodim_images")):
        ori_image = cv2.imread("kodim_images/" + image)
        stego_image = cv2.imread("reconstruction_images/" + image)
        ssim = SSIM(ori_image, stego_image)
        diff = ori_image - stego_image
        MSE = (diff ** 2).mean(axis=None)
        PSNR = 10 * np.log10(255 * 255 / MSE)

        meas = PSNR

        sum += meas
        len += 1

        if min > meas:
            min = meas

        if max < meas:
            max = meas

        print(round(meas, 4))

    print("average:", round(sum / len, 4))
    print("max:", round(max, 4))
    print("min:", round(min, 4))


def measure(img1, img2):
    cover_image = cv2.imread(img1)
    stego_image = cv2.imread(img2)

    diff = cover_image - stego_image
    MSE = (diff ** 2).mean(axis=None)
    if not MSE:
        return 0, "inf", 1.0

    PSNR = 10 * np.log10(255 * 255 / MSE)
    ssim = SSIM(cover_image, stego_image)

    diff[diff != 0] = 255

    return round(MSE, 4), round(PSNR, 4), round(ssim, 4)
