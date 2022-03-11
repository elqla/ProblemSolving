import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    if n==1:
        print(max(arr[0][0], arr[1][0]))
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        # a, b, c  <c>
        # d, e, f  c, e, a.../ c, d...
        for i in range(2, n):
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
        print(max(arr[0][n-1], arr[1][n-1]))




    # dp = [[0]*n, [0]*n]
    # dp[0][0] = arr[0][0]
    # dp[1][0] = arr[1][0]
    #
    # dp[0][1] = dp[1][0] + arr[0][1]
    # dp[1][1] = dp[0][0] + arr[1][1]
    #
    # for i in range(2, n):
    #     # dp[0][i]번째에 올 수 있는 최대값을 누적해서 저장한다.
    #     dp[0][i] = max(arr[0][i] + dp[1][i-1], arr[0][i] + dp[1][i-2])
    #     # a, b, c, d    g를 구하려면, g-b-e/g-a
    #     # e, f, g, h    d를 구하려면, d-g-b/d-f
    #     dp[1][i] = max(arr[1][i] + dp[0][i-1], arr[1][i] + dp[0][i-2])
    #
    # print(max(dp[0][n-1], dp[1][n-1]))