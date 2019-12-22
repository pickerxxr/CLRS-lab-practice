def numDecodings(s):
    dp = [0 for i in range(len(s) + 1)]
    for i in range(len(s) + 1):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            if s[i - 1] == '0':
                return 0
            else:
                dp[i] = 1
        else:
            if s[i - 1] == '0':
                if int(s[i - 2]) <= 2 and int(s[i - 2]) >= 1:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                dp[i] = dp[i - 1]
                if int(s[i - 2:i]) <= 26 and int(s[i - 2:i]) >= 11:
                    dp[i] += dp[i - 2]
    if s == '':
        return 0
    return dp[-1]

a = '22617'
print(numDecodings(a))