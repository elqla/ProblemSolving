from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ax, ay = n-1, m-1 #도착지점
# 0, 0에서 출발

dq = deque([[0, 0]])
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
while dq:
    x, y = dq.popleft()
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
            if visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y] + 1
                dq.append((nx, ny))
            elif visited[nx][ny] <= visited[x][y]: # 앞에서 0일때 처리하므로 방문 한곳이라는 것
                continue
            elif visited[nx][ny] > visited[x][y]:
                visited[nx][ny] = visited[x][y] + 1

print(visited[-1][-1])
