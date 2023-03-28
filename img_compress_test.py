import os
import matplotlib.pyplot as plt
import cv2
from measure import *
from embedded_methods import *
import numpy as np
from convert import *

def float_rgb(r, g, b):
    return r / 255, g / 255, b / 255


def hsv(r, g, b, C_max, delta):
    if delta == 0:
        h = 0
    elif C_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif C_max == g:
        h = 60 * ((b - r) / delta + 2)
    else:
        h = 60 * ((r - g) / delta + 4)

    h = round(h, 1)

    if C_max == 0:
        s = 0
    else:
        s = round(delta / C_max * 100, 1)

    v = round(C_max * 100, 1)
    return h, s, v


def embed1(channels, message):
    Min = [2, 2, 2]

    for index, channel in enumerate(channels):
        f_from = round(channel) - 1
        f_to = round(channel) + 2

        for k in range(f_from, f_to):
            if k % 3 == message[index] and abs(k - channel) < Min[index]:
                Min[index] = round(k - channel, 1)

        channels[index] += Min[index]

    return channels


def WM_color(N, M, image_name, secret, file_len=0):
    img = cv2.imread(image_name)
    h, w, c = img.shape
    img = img.reshape(-1)
    weight = np.arange(N) + 1
    print("len = ", img.size)
    print("sec = ", len(secret))
    i = 0

    while True:
        segment = secret[i * N: (i + 1) * N]

        if not segment:
            break

        octal_val = int(segment, 2)

        img[i * N: (i + 1) * N] = embed(img[i * N: (i + 1) * N], weight, M, octal_val)
        i += 1

    data1, data2 = extract(img, weight, M, i, file_len)
    return img.reshape(h, w, c)


def compress():
    os.system("opj_compress.exe -i images/Lena.bmp -o compressed1.jp2 -r 16 -I True")
    os.system("opj_compress.exe -i images/Peppers.bmp -o compressed2.jp2 -r 16 -I True")


def decompress():
    os.system("opj_decompress.exe -i compressed1.jp2 -o Lena1.bmp")
    os.system("opj_decompress.exe -i compressed2.jp2 -o Peppers1.bmp")


if __name__ == "__main__":
    compress()

    # img1 = cv2.imread("Peppers.bmp")
    # img2 = cv2.imread("Peppers1.bmp")

    file = file_to_bin("compressed1.jp2", "compressed2.jp2")

    data = bin_to_data(file)
    # data2 = bin_to_data(file[file1_length * 8:])
    print(data)
    # stego_img = WM_color(3, 8, "Baboon.bmp", file, file1_length)

