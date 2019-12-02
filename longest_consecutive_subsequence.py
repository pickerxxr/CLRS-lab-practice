def longest_cs(arr):
    a = {}
    for i in arr:
        a[i] = i
    maxlen = 0
    for i in arr:
        if (i - 1) not in a:
            cnt = 1
            head = i
            while((head + 1) in a):
                head += 1
                cnt += 1
            maxlen = max(maxlen, cnt)
    return maxlen
