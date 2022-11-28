
def is_prime(n):
    if(n==1): return False
    for i in range(2, n//2+1):  #절반 이상의 수는 필요없음
        if n%i == 0:
            return False #i로 나누어 떨어지면 소수가 아님
    return True


# 소수: 1을 제외한 수 중, 1과 자기 자신만을 약수로 가지는 수
t = int(input())
cnt = 0
num_lst = list(map(int, input().split()))
for num in num_lst:
    res = is_prime(num)
    if(res): cnt += 1

print(cnt)