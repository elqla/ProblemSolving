#1, 1/  2, 2 / 3, 3 / 4, 5 / 5 , 8 (n, 타일개수)
n = int(input())
dp = [0]*(n+1)
for i in range(1, n+1):
    if i==1 or i==2:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
        
res = dp[n]%10007
print(res)



