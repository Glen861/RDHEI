from math import sin

import numpy as np
from constants import *


def Gen_Float_Seq(length):
    mu = 1.2
    i1, i2, i3 = init_value
    x = [i1]
    y = [i2]
    z = [i3]
    sequence = []

    length = length // 3 + 1
    for i in range(1, length+2):
        x.append((mu * k1 * y[i-1] * (1-x[i-1]) + z[i-1]) % 1)
        y.append((mu * k2 * y[i-1] + (z[i-1] / (1 + pow(x[i], 2)))) % 1)
        z.append((mu * (x[i] + y[i] + k3) * sin(z[i-1])) % 1)

    sequence += x
    sequence += y
    sequence += z

    return np.array(sequence)


def Gen_Int_Seq(length, N=2):
    sequence = Gen_Float_Seq(length)

    sequence = np.round(sequence * pow(2, 24))
    sequence = np.mod(sequence, N)
    return sequence.astype(int)


if __name__ == '__main__':
    pass
