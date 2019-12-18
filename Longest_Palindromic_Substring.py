# dynamic programming
def Longest_Palindromic_Substring(str):
    lo = len(str)
    arr = [[0 for i in range(lo)]for i in range(lo)]
    for i in range(0, lo):
        arr[i][i] = 1
    for m in range(1, lo):
        for mi in range(0, lo - m):
            if str[mi] == str[mi + m]:
                arr[mi][m + mi] = 2 + arr[mi + 1][m + mi -1]
            else:
                arr[mi][mi + m] = max(arr[mi + 1][mi + m], arr[mi][mi + m - 1])
    return arr[0][lo - 1]


for_test  = 'abandna'
print(Longest_Palindromic_Substring((for_test)))
