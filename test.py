import random
import cv2
import numpy as np
from pywt import dwt2, idwt2

from Compress import *
from Decompress import *
from Convert_File_Binary import *
from Decrypt import Decrypt
from Encrypt import Encrypt
from measure import PSNR

import matplotlib.pyplot as plt
from imageio import imread


# from 1nt_toolbox.general import *
# from nt_toolbox.signal import *
# from nt_toolbox.compute_wavelet_filter import *


def test():
    # compress("Images")
    # decompress("Compress_file")
    directory = 'Compress_file'

    file1 = f"{directory}//compressed_Lena.jp2"
    file2 = f"{directory}//compressed_Peppers.jp2"
    file3 = f"{directory}//compressed_Baboon.jp2"

    data = file_to_bin([file1, file2, file3])
    secret = ''.join(str(random.randint(0, 1)) for e in range(100))
    data = add_secret(data, secret)

    file, msg = bin_to_file(data)
    write_data(file)

    print(msg == secret)


def display(im):  # Define a new Python routine
    """
    Displays an image using the methods of the 'matplotlib' library.
    """
    plt.figure(figsize=(8, 8))  # Square blackboard
    plt.imshow(im, cmap="gray", vmin=0, vmax=1)  # Display 'im' using a gray colormap,

    #         from 0 (black) to 1 (white)


def display_2(im_1, title_1, im_2, title_2):
    """
    Displays two images side by side; typically, an image and its Fourier transform.
    """
    plt.figure(figsize=(12, 6))  # Rectangular blackboard
    plt.subplot(1, 2, 1);
    plt.title(title_1)  # 1x2 waffle plot, 1st cell
    plt.imshow(im_1, cmap="gray")  # Auto-equalization
    plt.subplot(1, 2, 2);
    plt.title(title_2)  # 1x2 waffle plot, 2nd cell
    plt.imshow(im_2, cmap="gray", vmin=-1, vmax=1)  # Auto-equalizatio


def dwt():
    img = cv2.imread("Images/Lena.bmp", 0)
    cA, (cH, cV, cD) = dwt2(img, 'haar')

    # 小波變換後，低頻分量對應的圖像
    img1 = np.uint8(cA / np.max(cA) * 255)

    # 小波變換後，水平方向高頻分量對應的圖像
    img2 = np.uint8(cH / np.max(cH) * 255)

    # 小波變換後，垂直方向高頻分量對應的圖像
    img3 = np.uint8(cV / np.max(cV) * 255)

    # 小波變換後，對角方向高頻分量對應的圖像
    img4 = np.uint8(cD / np.max(cD) * 255)

    # 根據小波係數重構的圖像
    rimg = idwt2((cA, (cH, cV, cD)), 'haar')

    cv2.imwrite("dtw_cH.bmp", cH)

    plt.imshow(img4)

    # plt.show()


if __name__ == "__main__":
    # image1 = cv2.imread("Decompress_file//Peppers.bmp")
    # image2 = cv2.imread("Images//Peppers.bmp")
    # print(PSNR(image1, image2))
    #
    # img1 = cv2.imread("test1.bmp")
    # img2 = cv2.imread("test2.bmp")
    #
    # img1 = cv2.cvtColor(img1, cv2.COLOR_HSV2BGR)
    # img2 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)
    #
    # img3 = cv2.imread("Images/Peppers.bmp")
    # img4 = cv2.imread("Images/Baboon.bmp")
    #
    # print(PSNR(img1, img3))
    # print(PSNR(img2, img4))

    # import center_images

    # k = []
    # with open("Compress_file/compressed_test1.jp2", "rb") as fp:
    #     # print(fp.read()[1500:1510])
    #     while True:
    #         x = fp.read(1)
    #         if x:
    #             k.append(x)
    #         else:
    #             break
    #
    #     k = k[1500:1510]
    #
    #     for i in k:
    #         print(i, bin(int(i.hex(), 16))[2:].zfill(8))

    # dwt()

    # img = cv2.imread("ret.bmp")[:,:,0]
    # img1 = cv2.imread('ret1.bmp')[:,:,0]
    # print(PSNR(img, img1))
    # cv2.imwrite("Test_image/test1.bmp", img[:,:,::-1])
    #
    # Compress("Test_image")
    # Decompress("Compress_file")
    img1 = cv2.imread("Images/Lena.bmp")
    # img2 = cv2.imread("Decompress_file/Lena.bmp")
    # print(PSNR(img1, img2))

