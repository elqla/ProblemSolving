n = int(input())
dp = [[1 for _ in range(10)] for _ in range(n)]   #0, 1

if n== 1:
    pass
else:
    for i in range(1, n):  # n ==2; 1
        for j in range(10):
            dp[i][j] = sum(dp[i-1][j:])
print(sum(dp[n-1])%10007)