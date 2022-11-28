# from functools import lru_cache
# @lru_cache(maxsize=None)

dic = {
    0:0,
    1:1,
    2:1,
}

def fibo(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = fibo(n-1) + fibo(n-2)
        return dic[n]

print(fibo(int(input())))