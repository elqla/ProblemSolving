n = int(input())
dp = [[0]+[1 for _ in range(9)] for _ in range(n)]


if n==1:
    print(9%1000000000)
else:
    for i in range(1, n):
        for j in range(10):
            if j ==0:
                dp[i][j] = dp[i-1][1] #dp[0] 이면 '10'으로 앞에 1밖에 못온다.
            elif j == 9:
                dp[i][j] = dp[i-1][8] #dp[9] 이면 '89'로 앞에 8밖에 못온다.
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[n-1])%1000000000)