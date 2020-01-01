def candy_greedy(arr):
    arr_new = []
    for i in range(0, len(arr)):
        arr_new.append(1)
    for j in range(1, len(arr)):
        if arr[j] > arr[j - 1]:
            arr_new[j] = arr_new[j - 1] + 1
    for k in range(len(arr) - 2, -1, -1):
        if arr[k] > arr[k + 1]:
            arr_new[k] = max(arr_new[k + 1] + 1, arr_new[k])
    return arr_new
arr_a = [1,2,3,3,4,6,4,5,3,2,4]
print(candy_greedy(arr_a))