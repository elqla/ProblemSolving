t = int(input())
for tc in range(1, t+1):
    n = int(input())
    dp = [[0]*(n+2) for _ in range(2)]
    dp[0][0] = 1  # 1번째 리스트 idx가 zero, one을 나타냄
    dp[1][0] = 0  # 2번째 리스트 idx가 해당 n값을 나타냄

    dp[0][1] = 0
    dp[1][1] = 1


    if n==0:
        print(dp[0][n], dp[1][n])
    elif n==1:
        print(dp[0][n], dp[1][n])
    else:
        for i in range(2, n+1):
            dp[0][i] = dp[0][i-1] + dp[0][i-2]
            dp[1][i] = dp[1][i-1] + dp[1][i-2]
        print(dp[0][n], dp[1][n])