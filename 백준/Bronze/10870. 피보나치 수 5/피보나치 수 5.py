from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

#n번째 피보나치수 구하기
# n = int(input())
# res = 0
# for i in range(1, n+1): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     print(fibo(i))
#     res += fibo(i)

# print(res)
print(fibo(int(input())))