from BitPlanes_Rearrange import *
from BitStream_Compress import *


def BitPlanes_Compress(Plane, Block_size, L_fix, L):
    length = 1e10
    CSB = None
    type = None

    for t in range(4):
        origin_bits = BitPlanes_Rearrange(Plane, Block_size, t)
        compress_bits = BitStream_Compress(origin_bits, L_fix, L)
        if length > len(compress_bits):
            CSB = compress_bits
            length = len(compress_bits)
            type = t

    return CSB, type


if __name__ == "__main__":
    img = cv2.imread("Lena.bmp")[:, :, 0][0:10, 0:10]
    img = np.unpackbits(img).reshape([10, 10, 8])

    bit_plane1 = img[:, :, 0]

    CBS, type = BitPlanes_Compress(bit_plane1, 4, 3, 4)