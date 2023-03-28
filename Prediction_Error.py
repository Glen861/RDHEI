import numpy as np


def Prediction_Error(image):
    image = image.astype(int)

    h, w = image.shape
    PE_I = image.copy()
    num_of = 0
    overflow = [[], []]
    for i in range(1, h):
        for j in range(1, w):
            a = image[i - 1][j]
            b = image[i - 1][j - 1]
            c = image[i][j - 1]

            if b <= min(a, c):
                pv = max(a, c)

            elif b >= max(a, c):
                pv = min(a, c)

            else:
                pv = a + c - b

            pe = image[i][j] - pv
            if 0 > pe >= -127:
                abs_pe = abs(pe)
                PE_I[i][j] = (abs_pe % 128) + 128

            elif 0 <= pe <= 127:
                PE_I[i][j] = pe

            else:
                PE_I[i][j] = image[i][j]
                overflow[0].append(i)
                overflow[1].append(j)
                num_of += 1

    return PE_I, num_of, overflow
