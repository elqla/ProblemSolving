dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs():
    s = 1
    while stack:
        x, y = stack.pop()
        for a in range(4):
            nx, ny = x + dx[a], y + dy[a]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                stack.append((nx, ny))
                arr[nx][ny] = 2
    return s

    pass
t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]


    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    stack = []
    res = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 2
                stack.append((i, j))
                res += dfs()
    print(res)