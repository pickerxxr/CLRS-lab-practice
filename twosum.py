def whether_exist_sum(S, sum):
    hs = []
    ctr = 0
    for i in S:
        if sum - i not in hs:
            hs.append(i)
        else:
            ctr = 1

    return ctr


res = whether_exist_sum([1,4,5,6,3], 15)
print(res)