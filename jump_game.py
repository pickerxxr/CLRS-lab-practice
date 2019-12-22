def greedy_jump(arr):
    n = len(arr)
    farthest_point = 0
    for i in range(0, n):
        if i <= farthest_point:
            farthest_point = max(farthest_point, i + arr[i])
    return farthest_point >= n - 1


array = [2, 3, 1, 1, 4]
print(greedy_jump(array))


