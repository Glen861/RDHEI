import numpy as np


def Data_Extract(stego_I, num_emD):
    row, col = stego_I.shape
    exD = []
    num_exD = 0
    for pl in range(8):
        if num_exD == num_emD:
            break

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if num_exD == num_emD:
                    break

                secret = 0
                if stego_I[i, j] & pow(2, pl):
                    secret = 1
                    stego_I[i, j] -= pow(2, pl)

                exD.append(secret)
                num_exD += 1

    return np.array(exD)
