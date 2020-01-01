def wildcard_matching(s, p):
    m = len(p)
    n = len(s)
    arr = [[0 for i in range(m + 1)]for j in range(n + 1)]
    arr[0][0] = True
    for i in range(1, m + 1):
        arr[0][i] = False
    for j in range(1, n + 1):
        arr[j][0] = False
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            elif p[j - 1] == '?':
                arr[i][j] = arr[i - 1][j - 1]
            elif p[j - 1] == '*':
                arr[i][j] = arr[i - 1][j] or arr[i][j - 1]
            else:
                arr[i][j] = False
    return arr[n][m]


s = 'teacher'  # 对应的是n
p = '?ea*r'  # 对应的是m
print(wildcard_matching(s, p))