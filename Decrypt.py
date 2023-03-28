import numpy as np

from FY_Algorithm import recover
from Gen_Seq import Gen_Int_Seq


def Decrypt(image, order):
    h, w = image.shape
    image = image.flatten()
    permutation_seq = Gen_Int_Seq(image.size, 256)
    for i in range(image.size):
        image[i] ^= permutation_seq[i]

    image = recover(image, order)

    return image.reshape([h, w]).astype(np.uint8)
