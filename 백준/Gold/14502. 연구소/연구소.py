from itertools import combinations
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
wall = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            wall.append((i, j))

mx = 0 # 안전영역의 최대값
for comb in combinations(wall, 3):
    new_arr = [x[:] for x in arr]  # deepcopy
    for i, j in comb:
        new_arr[i][j] = 1

    virues = list(virus)
    while virues:
        i, j = virues.pop()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m and new_arr[ni][nj] == 0:
                new_arr[ni][nj] = 2
                virues.append((ni, nj))

    mx_v = 0
    for a in new_arr:
        mx_v += a.count(0)
    if mx < mx_v:
        mx = mx_v

print(mx)