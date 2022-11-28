import math

def is_prime(n):
    if(n==1): return False
    for i in range(2, int(math.sqrt(n))+1): #n의 제곱근을 정수화한 후 + 1
        if n % i == 0:
            return False
    return True

# 소수: 1을 제외한 수 중, 1과 자기 자신만을 약수로 가지는 수
t = int(input())
cnt = 0
num_lst = list(map(int, input().split()))
for num in num_lst:
    res = is_prime(num)
    if(res): cnt += 1

print(cnt)