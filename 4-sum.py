# four sum
# [1, 4, 6, -2, -4, -3, -1, 9, 7, -5]

def four_sum(arr):
    hash_set = {}
    res = []
    l = len(arr);
    for i in range(0, l):
        for j in range(i + 1, l):
            key = arr[i] + arr[j]
            if key not in hash_set.keys():
                hash_set[key] = [(i, j)]
            else:
                hash_set[key].append((i, j))

    for m in range(0, l):
        for n in range(m + 1, l):
            tmp = - (arr[m] + arr[n])
            if tmp in hash_set.keys():
                for tmp_index in hash_set[tmp]:
                    if tmp_index[0] > n:
                        res.append([arr[m], arr[n], arr[tmp_index[0]], arr[tmp_index[1]]])

    return res


for_test = [4, 1, -2, -4, -3]
print(four_sum(for_test))
