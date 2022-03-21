import sys
input = sys.stdin.readline

n, m = map(int, input().split())
from math import sqrt

for num in range(n, m+1):
    if num != 1 and num % 2:
        for deno in range(3, int(sqrt(num))+1, 2):    # if 9 면, 3%3이 0이라서, else문이 실행되지 않는다.
            if num % deno == 0:                       # if 3~6 까지는 range가 3,3으로 같기 때문에 for문을 돌지 못하므로, else문이 실행된다.
                break
        else:
            print(num)  # break에 걸리지 않을시, 실행됨.
    elif num == 2:
        print(num)