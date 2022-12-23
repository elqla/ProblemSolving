
from collections import deque
'''
하루지나면 익은거 상하좌우로 토마토 익음
언제 토마토 다 익는지 최소일수
토마토 없을 수도 있음
'''

m, n = map(int, input().split())
tomato_arr = [list(map(int, input().split())) for _ in range(n)]
visited_arr = [[0]*m for _ in range(n)]

dq = deque() # 익은 토마토이면서 방문하지 않은 곳
for i in range(n):
    for j in range(m):
        if tomato_arr[i][j] == 1:
            visited_arr[i][j] = 1
            dq.append([i, j])
        elif tomato_arr[i][j] == -1:
            visited_arr[i][j] = -1

while dq:
    i, j = dq.popleft()
    for di, dj in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
         ni, nj = i + di, j + dj
         if 0<=ni<n and 0<=nj<m and visited_arr[ni][nj]==0:
             visited_arr[ni][nj] = visited_arr[i][j] + 1
             dq.append([ni, nj])


'''
모든 토마토가 익은 상태면 0 출력
모두 다 익지 못하는 상태면 -1 출력

# 0이 없을때
-1을 제외한 모든 수가 1이상이면 mx-1 출력

# 0이 있을때
다 못익은 상태이므로 -1 출력
'''
mx = 0
flag = False

for lst in visited_arr:
    if max(lst) > mx:
        mx = max(lst)
    for l in lst:
        if l == 0:
            flag = True
    if flag:
        mx = 0
        break

print(mx-1)