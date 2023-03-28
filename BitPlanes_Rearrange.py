import math
import cv2
import numpy as np
from BitPlanes_Compress import *


def BitPlanes_Rearrange(plane, Block_size, type):
    h, w = plane.shape
    m = math.floor(h / Block_size)
    n = math.floor(w / Block_size)
    origin_bits = np.zeros(plane.size, dtype=np.uint8)
    num = 0

    if type == 0:
        for i in range(m):
            for j in range(n):
                begin_x = i * Block_size
                begin_y = j * Block_size
                end_x = (i + 1) * Block_size
                end_y = (j + 1) * Block_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        origin_bits[num] = plane[x][y]
                        num += 1

            if w - n * Block_size > 0:
                begin_y = n * Block_size
                end_y = w
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if h - m * Block_size > 0:
            begin_x = m * Block_size
            end_x = h
            for j in range(n):
                begin_y = j * Block_size
                end_y = (j+1) * Block_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if h - m * Block_size > 0 and w - n * Block_size > 0:
            begin_x = m * Block_size
            begin_y = n * Block_size
            end_x = h
            end_y = w
            for x in range(begin_x, end_x):
                for y in range(begin_y, end_y):
                    origin_bits[num] = plane[x][y]

    if type == 1:
        for j in range(n):
            for i in range(m):
                begin_x = i * Block_size
                begin_y = j * Block_size
                end_x = (i + 1) * Block_size
                end_y = (j + 1) * Block_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        origin_bits[num] = plane[x][y]
                        num += 1

            if w - m * Block_size > 0:
                begin_y = m * Block_size
                end_y = h
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if w - n * Block_size > 0:
            begin_y = m * Block_size
            end_y = h
            for i in range(m):
                begin_x = i * Block_size
                end_x = (i + 1) * Block_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if h - m * Block_size > 0 and w - n * Block_size > 0:
            begin_x = m * Block_size
            begin_y = n * Block_size
            end_x = h
            end_y = w
            for x in range(begin_x, end_x):
                for y in range(begin_y, end_y):
                    origin_bits[num] = plane[x][y]

    if type == 2:
        for i in range(m):
            for j in range(n):
                begin_x = i * Block_size
                begin_y = j * Block_size
                end_x = (i + 1) * Block_size
                end_y = (j + 1) * Block_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        origin_bits[num] = plane[x][y]
                        num += 1

            if w - n * Block_size > 0:
                begin_y = n * Block_size
                end_y = w
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if h - m * Block_size > 0:
            begin_x = m * Block_size
            end_x = h
            for j in range(n):
                begin_y = j * Block_size
                end_y = (j+1) * Block_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if h - m * Block_size > 0 and w - n * Block_size > 0:
            begin_x = m * Block_size
            begin_y = n * Block_size
            end_x = h
            end_y = w
            for y in range(begin_y, end_y):
                for x in range(begin_x, end_x):
                    origin_bits[num] = plane[x][y]

    if type == 3:
        for j in range(m):
            for i in range(n):
                begin_x = i * Block_size
                begin_y = j * Block_size
                end_x = (i + 1) * Block_size
                end_y = (j + 1) * Block_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        origin_bits[num] = plane[y][x]      # change
                        num += 1

            if h - m * Block_size > 0:
                begin_y = m * Block_size
                end_y = h
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if w - n * Block_size > 0:
            begin_x = n * Block_size
            end_x = w
            for i in range(m):
                begin_y = i * Block_size
                end_y = (i+1) * Block_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        origin_bits[num] = plane[x][y]
                        num += 1

        if h - m * Block_size > 0 and w - n * Block_size > 0:
            begin_x = m * Block_size
            begin_y = n * Block_size
            end_x = h
            end_y = w
            for y in range(begin_y, end_y):
                for x in range(begin_x, end_x):
                    origin_bits[num] = plane[x][y]

    return origin_bits
