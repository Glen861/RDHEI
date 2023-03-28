from Prediction_Error import *
from Vacate_Room import *


def Vacate_Encrypt(origin_I, Block_size, L_fix, L):
    row, col = origin_I.shape
    num = int(np.ceil(np.log2(row)) + np.ceil(np.log2(col)) + 3)
    PE_I, num_Of, Overflow = Prediction_Error(origin_I)
    vacate_I, PL_len, PL_room, total_room = Vacate_Room(PE_I, Block_size, L_fix, L, num_Of, Overflow)

    if total_room >= num:
        bit_room = np.zeros(num, dtype=int)
        bit2_room = list(map(int, list(bin(total_room)[2:])))
        length = len(bit2_room)
        bit_room[num - length: num] = bit2_room
        for i in range(num):
            j = col - num + i
            vacate_I[row-1, j] = vacate_I[row-1, j] - vacate_I[row-1, j] % 2 + bit_room[i]

    return vacate_I, num_Of, PL_len, PL_room, total_room


if __name__ == '__main__':
    img = cv2.imread("block.bmp")[:, :, 0]
    vacate_I, num_Of, PL_len, PL_room, total_room = Vacate_Encrypt(img, 4, 3, 4)
    print(vacate_I)
