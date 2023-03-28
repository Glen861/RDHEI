import random
import sys

import cv2
import numpy as np
from Data_Embed import *
from Data_Extract import *
from Decrypt import Decrypt
from Encrypt import Encrypt
from Image_Recover import *
from Vacate_Encrypt import *
from Convert_File_Binary import *
from Compress import *

origin_I = cv2.imread("Images/kodim15.bmp")[:, :, ::-1][:, :, 0]

Block_size = 4
L_fix = 3
L = 4

# ----------------------------- 準備嵌入的影像 ----------------------------
Compress("Test_image")
directory = 'Compress_file'
file = [os.path.join(directory, file) for file in os.listdir(directory)]

print('\nEmbedding Image:')
for image in file:
    print(os.path.basename(image))
# ------------------------------- 秘密訊息 -------------------------------
# data = np.random.randint(2, size=3000000, dtype=int)
secret = ''.join(str(random.randint(0, 1)) for e in range(100000))
data = list(map(int, list(file_to_bin(file))))

data_len = len(data)
print(f"Two Image Length: {data_len} bits\n")

data = add_secret(data, secret)


ES_I, num_Of, PL_len, PL_room, Total_Room = Vacate_Encrypt(origin_I, Block_size, L_fix, L)

row, col = origin_I.shape
num = np.ceil(np.log2(row)) + np.ceil(np.log2(col))+2
if Total_Room >= num:
    stego_I, emD = Data_Embed(ES_I, data)
    num_emD = len(emD)
    if num_emD < data_len:
        print(f"Emd Length: {num_emD} bits")
        print("Fail To Hide Two Color Image.")
        sys.exit()

    # ------------------------------- 影像加密 -------------------------------
    enc_stego_I, order = Encrypt(stego_I)
    cv2.imwrite("enc_I.bmp", enc_stego_I)
    # ------------------------------- 影像解密 -------------------------------
    stego_I = Decrypt(enc_stego_I, order)

    # ------------------------------- 資料提取 -------------------------------
    exD = Data_Extract(stego_I, num_emD)

    # ------------------------------- 復原影像 -------------------------------
    recover_I = Image_Recover(stego_I)

    # ------------------------------- 執行結果 -------------------------------
    bpp = num_emD / origin_I.size

    if np.array_equal(emD, exD):
        print("Extracting Data Same as Embedding Data!")
    else:
        print("Warning! Wrong Extracting Data!")

    if np.array_equal(origin_I, recover_I):
        print("Same Image!")
    else:
        print("Two Image are Different!")

    file, msg = bin_to_file(exD)
    print(f"Total: {num_emD} bits")
    print(f"Extra Space: {Total_Room - num_emD} bits")
    print(f"Extra Secret: {len(msg)} bits")
    print(f"Bpp: {round(bpp, 4)}")

    write_data(file)




