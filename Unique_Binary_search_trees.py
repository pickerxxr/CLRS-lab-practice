def number_of_binary_search_tree(n):
    arr = [1, 1]
    for i in range(2, n + 1):
        tmp = 0
        for j in range(0, i):
            tmp += arr[j] * arr[i - j - 1]
        arr.append(tmp)
    return arr[n]


print(number_of_binary_search_tree(4))