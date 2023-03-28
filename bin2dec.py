def bin2dec(b):
    num = 0
    for i in range(len(b)):
        index = len(b) - i - 1
        if b[index]:
            num += pow(2, i)
    return num
