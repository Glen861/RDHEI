import cv2, os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import rgb2lab
from skimage import io, color


def save_img(image_name, img, color_space):
    if os.path.exists("ch1.png"): os.remove("ch1.png")
    if os.path.exists("ch2.png"): os.remove("ch2.png")
    if os.path.exists("ch3.png"): os.remove("ch3.png")

    if color_space != "YCbCr": order = [2,1,0]
    else: order = [1,0,2]
    ch1 = img[:, :, order[2]]
    ch2 = img[:, :, order[1]]
    ch3 = img[:, :, order[0]]

    cv2.imwrite("ch1.png", ch1)
    cv2.imwrite("ch2.png", ch2)
    cv2.imwrite("ch3.png", ch3)

    if color_space == "HSV":
        img = img[:,:,::-1]
    
    cv2.imwrite(image_name, img[:,:,::-1])


def RGB_to_HSV(image_name, image):
    img = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    save_img(image_name, img, "HSV")
    

def RGB_to_YIQ(image_name, image):
    image = image
    yiq_from_rgb = np.array([[0.299, 0.587, 0.114],
                             [0.59590059, -0.27455667, -0.32134392],
                             [0.21153661, -0.52273617, 0.31119955]])

    img_shape = image.shape
    YIQ = np.dot(image.reshape(-1,3), yiq_from_rgb.transpose()).reshape(img_shape)
     
    save_img(image_name, YIQ, "YIQ")
    

def RGB_to_CLELab(image_name, img):
    # img = rgb2lab.RGB_to_LAB(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    return img
    #save_img(image_name, img, "LAB")
     

def RGB_to_YCbCr(image_name, img):
    YCbCr = cv2.cvtColor(img, cv2.COLOR_RGB2YCR_CB)[:, :, ::-1]
    save_img(image_name, YCbCr, "YCbCr")
    

def YCbCr_to_RGB(image_name, img):
    RGB = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
    return RGB


def convert(image_name, img, color_space):
    if color_space == "RGB":
        save_img(image_name, img, "RGB")
    
    if color_space == "HSV":
        RGB_to_HSV(image_name, img)

    if color_space == "YIQ":
        RGB_to_YIQ(image_name, img)

    if color_space == "LAB":
        RGB_to_CLELab(image_name, img)

    if color_space == "YCbCr":
        RGB_to_YCbCr(image_name, img)


def construct(image_name, img, color_space):
    if color_space in ["HSV", "YIQ", "LAB"]:
        save_img(image_name, img, "RGB")
    #
    # else:
    #     img = reconstruct()
    #     YCbCr_to_RGB(image_name, img)
        

if __name__ == '__main__':
    img = cv2.imread("images/Lena.bmp")
    lab = RGB_to_CLELab(None, img)
    # print(lab)
    plt.imshow(lab)
    plt.show()


 









