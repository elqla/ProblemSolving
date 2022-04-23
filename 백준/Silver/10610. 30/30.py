# 각 자리수의 합이 3의 배수이면 3의 배수이다.

N = list(input())
N.sort(reverse=True)

mx = -1
res = sum(int(n) for n in N)

if N[-1]=='0' and res%3==0:
    mx = ''.join(N)

print(mx)