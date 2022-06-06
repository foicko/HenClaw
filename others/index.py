def Find_sec_max(ls):
    length = len(ls)
    qs = ls[:] * 2
    sec_max = -1
    # print(qs)
    print(qs[::-2])
    print(qs[:-1:][::-2])
    print(qs[length-1::-1])
    print(qs[-length-1::-1])
    qs[-length-1::-1] = max(qs[::-2], qs[:-1:][::-2])
    max_num = qs[1]
    print(qs)
    print(max_num)
    idx = 1
    while idx < length:
        if qs[idx * 2] == qs[idx]:
            if sec_max < qs[2 * idx + 1]:
                sec_max = qs[2 * idx + 1]
            idx = idx * 2
        else:
            if sec_max < qs[2 * idx]:
                sec_max = qs[2 * idx]
            idx = idx * 2 + 1
    return sec_max


print(Find_sec_max([1, 2, 3, 4, 5]))
