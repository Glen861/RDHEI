import numpy as np
from BitPlanes_Recover import *
from BitStream_DeCompress import *
from bin2dec import *


def Image_Recover(stego_I):
    row, col = stego_I.shape

    Image_Bits = []
    num_TB = 0
    bit_plane = np.unpackbits(stego_I.astype(np.uint8)).reshape([8, row, col], order='F')
    for i in range(8):
        Plane = bit_plane[i].T
        PL_bits = Plane.flatten().tolist()
        Image_Bits += PL_bits
        num_TB += row * col

    t = 0
    bin28_Bs = Image_Bits[t:t+4]
    Bloc_size = bin2dec(bin28_Bs)
    t += 4

    bin28_Lf = Image_Bits[t: t+3]
    L_fix = bin2dec(bin28_Lf)
    t += 3

    Overflow = [[], []]
    num = int(np.ceil(np.log2(row)) + np.ceil(np.log2(col)))
    bin2_num_Of = Image_Bits[t: t+num]
    t += num

    num_Of = bin2dec(bin2_num_Of)
    if num_Of > 0:
        for i in range(num_Of):
            bin2_pos = Image_Bits[t: t+num]
            t += num
            pos = bin2dec(bin2_pos)
            x = np.ceil(pos / col)
            y = pos - (x - 1) * col
            Overflow[0].append(x)
            Overflow[1].append(y)

    RI = np.zeros([8, row, col], dtype=int)
    for pl in range(8):
        sign = Image_Bits[t]
        t += 1
        if sign == 1:
            bin2_type = Image_Bits[t: t+2]
            type = bin2dec(bin2_type)
            t += 2

            bin2_len = Image_Bits[t: t+num]
            len_CBS = bin2dec(bin2_len)

            t += num
            CBS = Image_Bits[t: t+len_CBS]
            t += len_CBS
            Plane_bits = BitStream_DeCompress(CBS, L_fix)
            Plane_Matrix = BitPlanes_Recover(Plane_bits, Bloc_size, type, row, col)
        else:
            Plane_bits = np.array(Image_Bits[t: t+row*col])
            t += row*col
            Plane = Plane_bits.reshape(row, col)
            Plane_Matrix = Plane

        RI[pl] = Plane_Matrix
    stego_I = np.packbits(RI, axis=0)[0]

    recover_I = stego_I.copy().astype(int)
    k = 0
    for i in range(1, row):
        for j in range(1, col):
            if k < num_Of:
                if i == Overflow[0][k] and j == Overflow[1][k]:
                    k += 1
                    recover_I[i][j] = stego_I[i][j]

                else:
                    a = recover_I[i-1, j]
                    b = recover_I[i-1, j-1]
                    c = recover_I[i, j - 1]
                    if b <= min(a, c):
                        pv = max(a, c)
                    elif b >= max(a, c):
                        pv = min(a, c)
                    else:
                        pv = a + c - b

                    value = recover_I[i, j]
                    if value > 128:
                        pe = value - 128
                        recover_I[i, j] = pv - pe

                    else:
                        pe = value
                        recover_I[i, j] = pv + pe

            else:
                a = recover_I[i - 1, j]
                b = recover_I[i - 1, j - 1]
                c = recover_I[i, j - 1]

                if b <= min(a, c):
                    pv = max(a, c)
                elif b >= max(a, c):
                    pv = min(a, c)
                else:
                    pv = a + c - b

                value = recover_I[i, j]
                if value > 128:
                    pe = value - 128
                    recover_I[i, j] = pv - pe

                else:
                    pe = value
                    recover_I[i, j] = pv + pe

    return recover_I
