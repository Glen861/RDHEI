import cv2, math
import numpy as np
from BitPlanes_Compress import *


def Vacate_Room(PE_I, block_size, L_fix, L, num_of, overflow):
    h, w = PE_I.shape
    num = math.ceil(math.log2(h)) + math.ceil(math.log2(w))
    side = []
    num_side = 0

    bin_BS = "{:04b}".format(block_size)
    side[: 4] = list(map(int, bin_BS))
    num_side += 4

    bin_LF = "{:03b}".format(L_fix)
    side[num_side: num_side+3] = list(map(int, bin_LF))
    num_side += 3

    len_num_of = [0 for _ in range(num)]
    bin_num_of = bin(num_of)[2:]
    length = len(bin_num_of)
    len_num_of[num-length: num] = list(map(int, bin_num_of))
    side[num_side: num_side+num] = len_num_of
    num_side += num

    if num_of > 0:
        for i in range(num_of):
            x = overflow[0][i]
            y = overflow[1][i]
            pos = x * w + y + 1
            len_pos = [0 for _ in range(num)]
            bin_pos = bin(pos)[2:]
            length = len(bin_pos)
            len_pos[num-length: num] = list(map(int, bin_pos))
            side[num_side: num_side+num] = len_pos
            num_side += num

    Image_bits = side
    t = num_side

    PL_room = [0, 0, 0, 0, 0, 0, 0, 0]    # 紀錄空出後的大小
    PL_len = [0, 0, 0, 0, 0, 0, 0, 0]     # 紀錄壓縮後的bit長度
    num_pl = 0
    bit_plane = np.unpackbits(PE_I.astype(np.uint8)).reshape([8, h, w], order='F')
    for i in range(8):
        plane = bit_plane[i].T
        CBS, type = BitPlanes_Compress(plane, block_size, L_fix, L)
        len_CBS = len(CBS)
        len_comp_PL = len_CBS + num + 2 + 1

        if len_comp_PL <= h * w:
            num_pl += 1
            Image_bits.append(1)
            t += 1

            bin2_type = list(map(int, list(bin(type)[2:].zfill(2))))
            Image_bits += bin2_type
            t += 2

            len_CBS_bits = np.zeros(num, dtype=int)
            bin2_len_CBS = list(map(int, list(bin(len_CBS)[2:].zfill(num))))
            length = len(bin2_len_CBS)
            len_CBS_bits[num - length: num] = bin2_len_CBS
            Image_bits = Image_bits + len_CBS_bits.tolist()
            t += num
            Image_bits += CBS
            t += len_CBS

            PL_len[i] = len_CBS
            room = h * w - len_comp_PL
            PL_room[i] = room

        else:
            Image_bits.append(0)
            t += 1
            T_Plane = np.array(plane)
            PL_bits = T_Plane.flatten().tolist()
            Image_bits += PL_bits
            t += h * w

    num_t = 0
    RI = np.zeros([8, h, w], dtype=np.uint8)

    for i in range(8):
        re = t - num_t
        if re >= h * w:
            PL_bits = np.array(Image_bits[num_t: num_t + h * w])
            num_t += h * w
        else:
            PL_bits = np.zeros(h * w, dtype=int)
            PL_bits[: re] = Image_bits[num_t: num_t+re]
            num_t += re

        Plane = PL_bits.reshape(h, w)
        RI[i] = Plane

    RI = np.packbits(RI, axis=0)
    total_room = h * w * 8 - t
    return RI[0], PL_len, PL_room, total_room


