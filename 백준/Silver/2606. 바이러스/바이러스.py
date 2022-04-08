from collections import defaultdict
v = int(input()) # 컴퓨터 수
e = int(input())

network = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    network[a] += [b]
    network[b] += [a]

# 1번 컴퓨터가 바이러스에 걸렸다. 바이러스에 걸린 컴퓨터의 수는 ?
stack = []
visited = []
stack.append(1)
visited.append(1)
while stack:
    tmp = stack.pop()
    for com in network[tmp]:
        if com not in visited:
            visited.append(com)
            stack.append(com)
            
print(len(visited)-1)