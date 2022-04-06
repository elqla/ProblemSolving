n = int(input())
lst = [int(input()) for _ in range(n)]+[0, 0]

dp = [0]*(n+2)
dp[0] = lst[0]
dp[1] = lst[0]+lst[1]
dp[2] = max(lst[0]+lst[2], lst[1]+lst[2], dp[1])
if len(lst)>3:
    for i in range(3, n):
        dp[i] = max(lst[i]+dp[i-2], lst[i]+lst[i-1]+dp[i-3], dp[i-1])

print(max(dp))