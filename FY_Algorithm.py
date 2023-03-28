import numpy as np


def diffusion(matrix, seq):
    w = len(matrix)
    k = []
    for i in range(w):
        float_num = seq[i] * (w - i)
        num = int(np.floor(abs(float_num)))
        k.append(num)
        matrix[w - i - 1], matrix[num] = matrix[num], matrix[w - i - 1]

    return matrix, k


def recover(matrix, seq):
    length = len(matrix)
    last = length - 1
    for i in range(1, length):
        last -= 1
        random_index = seq[last]
        matrix[random_index], matrix[i] = matrix[i], matrix[random_index]

    return matrix