from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
dq = deque()
for _ in range(n):
    words = input().split()
    if len(words)==1:
        word = words[0]
    else:
        word, x = words[0], words[1]


    if word == 'push_front':
        dq.appendleft(x)
    elif word == 'push_back':
        dq.append(x)
    elif word == 'pop_front':
        if not dq:
            print(-1)
        else:
            tmp = dq.popleft()
            print(tmp)
    elif word == 'pop_back':
        if not dq:
            print(-1)
        else:
            tmp = dq.pop()
            print(tmp)
    elif word == 'size':
        print(len(dq))
    elif word == 'empty':
        if dq:
            print(0)
        else:
            print(1)


    elif word == 'front':
        if not dq:
            print(-1)
        else:
            tmp = dq[0]
            print(tmp)
    elif word == 'back':
        if not dq:
            print(-1)
        else:
            tmp = dq[-1]
            print(tmp)