# 1로 시작한다
# 1이 두번연속 X
n = int(input())
dp = [0, 1, 1]
for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n])

