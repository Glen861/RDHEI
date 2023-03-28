import struct
from constants import compress_len
from Decompress import *


def add_secret(data, secret):
    data += '0'
    data += secret
    return data


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


def file_to_bin(files):
    secret = ""
    for file in files:
        data, length = message(file)
        length = bin(length * 8)[2:].zfill(compress_len)  # 前 22 bits 用來儲存一張壓縮影像的長度
        secret += '1'           # 1 代表影像 0 代表資訊
        secret += length
        secret += data

    return secret


def bin_to_file(sequence):
    sequence = ''.join(str(e) for e in sequence)
    file = []
    secret_msg = []
    end = 1

    while end:
        if len(sequence):
            data = b''
            flag = sequence[0]
            sequence = sequence[1:]

            if flag == '1':                 # 代表此區段是影像
                length = sequence[:compress_len]
                length = int(length, 2) // 8
                sequence = sequence[compress_len:]
                for i in range(length):
                    segment = sequence[i * 8:(i + 1) * 8]
                    if segment == '':
                        break
                    segment = struct.pack('B', int(segment, 2))
                    data = b''.join([data, segment])

                file.append(data)
                sequence = sequence[length * 8:]

            else:                           # 代表後續是秘密訊息
                secret_msg = sequence
                end = 0
        else:
            end = 0

    return file, secret_msg


def write_data(file):
    for index, content in enumerate(file, 1):
        filename = f"Write_decompress//decompress{index}.jp2"
        with open(filename, "wb") as fp:
            fp.write(content)

    Decompress("Compress_file")

