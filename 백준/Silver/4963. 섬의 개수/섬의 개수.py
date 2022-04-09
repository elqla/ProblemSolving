import sys
input = sys.stdin.readline


delta = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (-1, 1), (0, -1 ), (0, 1)]
while True:
    w, h = map(int, input().split())
    if w==h==0:
        break
    arr = []
    for _ in range(h):
        lst = list(map(int, input().split()))
        arr.extend([lst])
    stack = []
    res = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                stack.append((i, j))
                arr[i][j] = 0
                res += 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0<=nx<h and 0<=ny <w and arr[nx][ny]==1:
                            arr[nx][ny] = 0
                            stack.append((nx, ny))
    print(res)
