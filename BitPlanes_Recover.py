import numpy as np


def BitPlanes_Recover(Plane_bits, Bloc_size, type, row, col):
    Plane_Matrix = np.zeros([row, col], dtype=int)
    m = int(np.floor(row/Bloc_size))
    n = int(np.floor(col/Bloc_size))
    num = 0

    if type == 0:
        for i in range(m):
            for j in range(n):
                begin_x = i * Bloc_size
                begin_y = j * Bloc_size
                end_x = (i + 1) * Bloc_size
                end_y = (j + 1) * Bloc_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

            if col - n * Bloc_size > 0:
                begin_y = n * Bloc_size
                end_y = col
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if row - m * Bloc_size > 0:
            begin_x = m * Bloc_size
            end_x = row
            for j in range(n):
                begin_y = j * Bloc_size
                end_y = (j + 1) * Bloc_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if row - m * Bloc_size > 0 and col - n * Bloc_size > 0:
            begin_x = m * Bloc_size
            begin_y = n * Bloc_size
            end_x = row
            end_y = col
            for x in range(begin_x, end_x):
                for y in range(begin_y, end_y):
                    Plane_Matrix[x, y] = Plane_bits[num]
                    num += 1

    elif type == 1:
        for j in range(n):
            for i in range(m):
                begin_x = i * Bloc_size
                begin_y = j * Bloc_size
                end_x = (i + 1) * Bloc_size
                end_y = (j + 1) * Bloc_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

            if row - m * Bloc_size > 0:
                begin_x = m * Bloc_size
                end_x = row
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if col - n * Bloc_size > 0:
            begin_y = n * Bloc_size
            end_y = row
            for i in range(m):
                begin_x = i * Bloc_size
                end_x = (i + 1) * Bloc_size
                for x in range(begin_x, end_x):
                    for y in range(begin_y, end_y):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if row - m * Bloc_size > 0 and col - n * Bloc_size > 0:
            begin_x = m * Bloc_size
            begin_y = n * Bloc_size
            end_x = row
            end_y = col
            for x in range(begin_x, end_x):
                for y in range(begin_y, end_y):
                    Plane_Matrix[x, y] = Plane_bits[num]
                    num += 1

    elif type == 2:
        for i in range(m):
            for j in range(n):
                begin_x = i * Bloc_size
                begin_y = j * Bloc_size
                end_x = (i + 1) * Bloc_size
                end_y = (j + 1) * Bloc_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

            if col - n * Bloc_size > 0:
                begin_y = n * Bloc_size
                end_y = col
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if row - m * Bloc_size > 0:
            begin_x = m * Bloc_size
            end_x = row
            for j in range(n):
                begin_y = j * Bloc_size
                end_y = (j + 1) * Bloc_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if row - m * Bloc_size > 0 and col - n * Bloc_size > 0:
            begin_x = m * Bloc_size
            begin_y = n * Bloc_size
            end_x = row
            end_y = col
            for y in range(begin_y, end_y):
                for x in range(begin_x, end_x):
                    Plane_Matrix[x, y] = Plane_bits[num]
                    num += 1

    elif type == 3:
        for j in range(n):
            for i in range(m):
                begin_x = i * Bloc_size
                begin_y = j * Bloc_size
                end_x = (i + 1) * Bloc_size
                end_y = (j + 1) * Bloc_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

            if row - m * Bloc_size > 0:
                begin_x = m * Bloc_size
                end_x = row
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if col - n * Bloc_size > 0:
            begin_y = n * Bloc_size
            end_y = row
            for i in range(m):
                begin_x = i * Bloc_size
                end_x = (i + 1) * Bloc_size
                for y in range(begin_y, end_y):
                    for x in range(begin_x, end_x):
                        Plane_Matrix[x, y] = Plane_bits[num]
                        num += 1

        if row - m * Bloc_size > 0 and col - n * Bloc_size > 0:
            begin_x = m * Bloc_size
            begin_y = n * Bloc_size
            end_x = row
            end_y = col
            for y in range(begin_y, end_y):
                for x in range(begin_x, end_x):
                    Plane_Matrix[x, y] = Plane_bits[num]
                    num += 1

    return Plane_Matrix