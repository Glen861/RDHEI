from bin2dec import bin2dec


def BitStream_DeCompress(compress_bits, L_fix):
    len_bits = len(compress_bits)
    comp_t = 0
    origin_bits = []
    ori_t = 0
    while comp_t < len_bits:
        label = compress_bits[comp_t]
        if label == 1:
            L_pre = 0
            for i in range(comp_t, len_bits):
                if compress_bits[i] == 1:
                    L_pre += 1
                else:
                    L_pre += 1
                    break

            comp_t += L_pre
            l_bits = compress_bits[comp_t: comp_t+L_pre]
            comp_t += L_pre

            l = bin2dec(l_bits)
            L = pow(2, L_pre) + l
            bit = compress_bits[comp_t]
            comp_t += 1
            for i in range(L):
                origin_bits.append(bit)
                ori_t += 1

        elif label == 0:
            if comp_t + L_fix + 1 <= len_bits:
                comp_t += 1
                origin_bits += compress_bits[comp_t:comp_t+L_fix]
                ori_t += L_fix
                comp_t += L_fix
            else:
                comp_t += 1
                re = len_bits - comp_t
                origin_bits += compress_bits[comp_t: comp_t+re]
                ori_t += re
                comp_t += re
        # print(ori_t)
    return origin_bits

