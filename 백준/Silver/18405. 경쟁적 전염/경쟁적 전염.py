n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
x = x-1
y = y-1

dq = []
for i in range(n):
    for j in range(n):
        if arr[i][j] !=0:
            dq.append((arr[i][j],i, j, 0))
dq.sort()
dq = dq
while dq:
    sort, i, j, time = dq.pop(0)
    if time == s:
        break
    else:
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0:
                arr[ni][nj] = sort
                dq.append((sort, ni, nj, time+1))


print(arr[x][y])