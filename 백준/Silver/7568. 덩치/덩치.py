
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for lst in arr:
    res = 1
    for compare_lst in arr:
        if compare_lst[0] >  lst[0] and compare_lst[1] > lst[1]:
            res += 1
    print(res, end=" ")