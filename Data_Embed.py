import numpy as np


def Data_Embed(ES_I, D):
    row, col = ES_I.shape
    num = int(np.ceil(np.log2(row)) + np.ceil(np.log2(col)) + 3)
    bits_room = ""

    for i in range(num):
        j = col-num+i
        bits_room += str(ES_I[row-1, j] % 2)
        ES_I[row - 1, j] = ES_I[row-1, j] - ES_I[row-1, j] % 2

    total_room = int(bits_room, 2)
    stego_I = ES_I.copy()
    num_D = len(D)
    num_emD = 0

    for pl in range(8):
        if num_emD == num_D or num_emD == total_room:
            break

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if num_emD == num_D or num_emD == total_room:
                    break

                stego_I[i, j] = stego_I[i, j] + pow(2, pl) * int(D[num_emD])
                num_emD += 1

    emD = D[: num_emD]
    emD = [int(i) for i in emD]

    return stego_I, np.array(emD)
