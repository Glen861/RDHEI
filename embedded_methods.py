import struct, cv2, time
import numpy as np
import os

from constants import compress_len


def extract_len(seq):
    file_len = b''

    for i in range(4):
        byte = seq[i * 8: (i + 1) * 8]
        segment = struct.pack('B', int(byte, 2))
        file_len = b''.join([segment, file_len])

    return struct.unpack("i", file_len)[0]


def message(filename):
    content_to_bin = ''
    file_len = 0
    with open(filename, "rb") as fp:
        while True:
            segment = fp.read(1)

            if not segment:
                break

            file_len += 1
            content_to_bin += bin(int(segment.hex(), 16))[2:].zfill(8)

    return content_to_bin, file_len


def file_to_bin(Cb_compressed, Cr_compressed):
    secret = ""

    data1, len_1 = message(Cb_compressed)
    len_1 = bin(len_1 * 8)[2:].zfill(compress_len)  # 前 22 bits 用來儲存一張壓縮影像的長度
    secret += len_1
    secret += data1

    data2, len_2 = message(Cr_compressed)
    len_2 = bin(len_2 * 8)[2:].zfill(compress_len)  # 前 22 bits 用來儲存一張壓縮影像的長度
    secret += len_2
    secret += data2

    return secret


def bin_to_data(sequence):
    sequence = ''.join(str(e) for e in sequence)
    data = b''
    i = 0

    while True:
        segment = sequence[i * 8:(i + 1) * 8]

        if segment == '':
            break

        segment = struct.pack('B', int(segment, 2))
        data = b''.join([data, segment])
        i += 1

    return data


def write_data(data1, data2):
    with open("decompress1.jp2", "wb") as fp:
        fp.write(data1)

    with open("decompress2.jp2", "wb") as fp:
        fp.write(data2)


def PA_table(n):
    table = np.array([[0, 0, 0], [1, 0, 0],
                      [0, 1, 0], [0, 0, 1],
                      [1, 0, 1], [0, 0, -1],
                      [0, -1, 0], [-1, 0, 0]])

    return table[n]


count = 0


def embed(pixels, weight, M, octal_val):
    r = np.dot(pixels, weight.T) % M
    d = (octal_val - r) % M
    pixels = pixels + PA_table(d)

    pixels[pixels == 256] = 255
    pixels[pixels == -1] = 0

    return pixels


def extract(stego_img, weight, M, length, file_len):
    seq = ''
    N = len(weight)

    for i in range(length):
        remain = np.dot(stego_img[i * N: (i + 1) * N], weight.T) % M

        seq += bin(remain)[2:].zfill(3)

    data1 = bin_to_data(seq[: file_len * 8])
    data2 = bin_to_data(seq[file_len * 8:])

    return data1, data2


def WM(N, M, image_name, secret, file_len=0):
    img = cv2.imread(image_name)[:, :, 0]
    h, w = img.shape
    img = img.reshape(-1)
    weight = np.arange(N) + 1

    i = 0

    while True:
        segment = secret[i * N: (i + 1) * N]

        if not segment:
            break

        octal_val = int(segment, 2)

        try:
            img[i * N: (i + 1) * N] = embed(img[i * N: (i + 1) * N], weight, M, octal_val)
        except:
            pass

        i += 1

    # write_data(*extract(img, weight, M, i, file_len), num)
    return img.reshape(h, w)


def LSB(image_name, secret, file_len=0):
    img = cv2.imread(image_name)[:, :, 0]

    h, w = img.shape
    img = img.reshape(-1)

    length = min(len(img), len(secret))
    for i in range(length):
        img[i] = img[i] - (img[i] % 2) + int(secret[i])

    return img.reshape(h, w)


def func(group, n):
    weight = np.array([i + 1 for i in range(n)])

    return group.dot(weight) % (2 * n + 1)


def EMD(image_name, secret, file_len=0):
    n = 3
    img = cv2.imread(image_name)[:, :, 0]
    h, w = img.shape
    img = img.reshape(-1)

    img[img == 255] = 254
    img[img == 0] = 1

    stego = img.copy()
    size = img.size

    for i in range(0, size, n):
        if (i + n) <= size:
            group = np.array([stego[i + k] for k in range(n)])
            d = np.random.randint(2 * n + 1)  # secret digit
            # secret_list1.append(d)

            f = func(group, n)
            s = int((d - f) % (2 * n + 1))

            if s == 0:
                pass

            elif s > n:
                s = 2 * n + 1 - s
                if (i + s - 1) < size:
                    stego[i + s - 1] -= 1

            else:
                if (i + s - 1) < size:
                    stego[i + s - 1] += 1

    return stego.reshape(h, w)


def compress():
    os.system("opj_compress.exe -i ch2.png -o compressed1.jp2 -r 16 -I True")
    os.system("opj_compress.exe -i ch3.png -o compressed2.jp2 -r 16 -I True")


def embedded_method(method):
    if method == "None": return

    compress()
    channel_1_compressed = "compressed1.jp2"
    channel_2_compressed = "compressed2.jp2"
    image_name = "ch1.png"
    secret, file_len = file_to_bin(channel_1_compressed, channel_2_compressed)

    if method == "LSB":
        stego_img = LSB(image_name, secret, file_len)

    elif method == "EMD":
        stego_img = EMD(image_name, secret, file_len)

    elif method == "WM":
        stego_img = WM(3, 8, image_name, secret, file_len)

    cv2.imwrite("stego_image.png", stego_img)
