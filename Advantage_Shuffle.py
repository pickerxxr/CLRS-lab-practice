# classic greedy
def advantage_shuffle(arr_1, arr_2):
    arr_1_ctr = sorted(arr_1)
    arr_1_new = []
    for i in arr_2:
        ctr = 0
        for j in arr_1_ctr:
            if j > i:
                arr_1_new.append(j)
                ctr = 1
                break
        if ctr == 0:
            arr_1_new.append(arr_1_ctr[0])
    return arr_1_new


a = [2, 7, 11, 15]
b = [1, 10, 4, 11]
c = [12, 24, 8, 32]
d = [13, 25, 32, 11]
print("A after shuffling:")
print(advantage_shuffle(a, b))
print("C after shuffling:")
print(advantage_shuffle(c, d))