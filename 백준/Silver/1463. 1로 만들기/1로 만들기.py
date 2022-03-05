from collections import defaultdict

def makeone(n):
    dp = defaultdict(int)
    if n <= 1:
        return 0
    else:
        for i in range(2, n+1):  # dp[1]은 연산할게 없어서 0 이므로 2부터 진행해준다.
            dp[i] = dp[i-1] +1   #dp[i-1] = dp[i]에서 -1을 적용하는 연산을 하나 추가해줄 수 있다.
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i // 3] + 1)  # dp[i//3]+ 1 은 예를 들어 dp[9]는 dp[9//3]에서 한번만 더 연산을 해주면 되기 때문
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)  # dp[6] 은 dp[6//3]-> 6/3=2 , 2/2=1  (dp[2]+1)
        return dp[i]
n = int(input())
print(makeone(n))