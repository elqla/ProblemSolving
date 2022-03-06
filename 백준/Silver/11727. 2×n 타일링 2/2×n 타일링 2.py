# n, (ㅣㅡ일때 타일수)+(ㅁ가 있을때) = 합계
# 1, 1
# 2, 2+1 = 3
#               dp[n-1] + dp[n-2]*2
# 3, 3+2 = 5        3   +  1*2
# 4, 5+6  11        5   +  3*2
from collections import defaultdict
n = int(input())
dp = defaultdict(int)
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[n] % 10007)
