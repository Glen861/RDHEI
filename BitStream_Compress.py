"""
Function：Compress Bit Stream
Input：origin_bits, L_fix, L
Output：compress_bits
"""
import numpy as np


def BitStream_Compress(origin_bits, L_fix, L):
    len_bits = len(origin_bits)
    ori_t = 0
    compress_bits = []
    comp_t = 0

    while ori_t < len_bits:
        bit = origin_bits[ori_t]
        same_bits = 0
        comp_L = []

        for i in range(ori_t, len_bits):
            if origin_bits[i] == bit:
                same_bits += 1
            else:
                break

        if same_bits < L:
            comp_L.append(0)
            if ori_t + L_fix <= len_bits:
                comp_L += origin_bits[ori_t: ori_t+L_fix].tolist()
                same_bits = L_fix
            else:
                re = len_bits - ori_t
                comp_L += (origin_bits[ori_t:ori_t+re]).tolist()
                same_bits = re

        else:
            L_pre = int(np.floor(np.log2(same_bits)))
            for i in range(L_pre-1):
                comp_L.append(1)
            comp_L.append(0)
            l = same_bits - pow(2, L_pre)
            bin_l = list(map(int, list(bin(l)[2:])))
            len_l = len(bin_l)
            while len(comp_L) < 2 * L_pre - len_l:
                comp_L.append(0)

            comp_L += bin_l
            comp_L.append(bit)

        len_L = len(comp_L)
        compress_bits += comp_L
        comp_t += len_L
        ori_t += same_bits

    return compress_bits


if __name__ == "__main__":
    pass
