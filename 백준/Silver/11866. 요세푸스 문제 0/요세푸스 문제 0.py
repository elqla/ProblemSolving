import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque([x for x in range(1, n+1)])

# 1234567  # 왼쪽에서 꺼냈을때 길이가 3이 아니면 
# 2345671  # 오른쪽으로 붙여 원 만들어 주기
# 3456712  # 3이면, 출력한 후
# 4567123  # 다음거부터 다시 l = 0으로 시작
print('<', end="")
res = []
l = 0
while dq:
    for i in range(m-1):
        dq.append(dq.popleft())
    print(dq.popleft(), end="")
    if dq:
        print(',', end=" ")
print('>')

    # l += 1
    # tmp = dq.popleft()
    # if l==3:
    #     l = 0
    #     res.append(str(tmp))
    # else:
    #     dq.append(tmp)

