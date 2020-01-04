count = 0
def queen(A, cur=0):
    if cur == len(A):
        print(A)
    else:
        for col in range(len(A)):
            A[cur] = col  # 表示把第cur行的皇后放在col列上
            ok = True
            for r in range(cur):
                if A[r] == col or r - A[r] == cur - A[cur] or r + A[r] == cur + A[cur]:  # 判断是否跟前面的皇后冲突
                    ok = False
                    break
            if ok:
                queen(A, cur + 1)



queen([None] * 8)