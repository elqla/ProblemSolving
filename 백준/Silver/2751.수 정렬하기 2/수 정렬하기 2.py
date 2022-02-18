N = int(input())
arr = [int(input()) for _ in range(N)]

for i in sorted(arr):
    print(i)
'''
N = int(input())   #5
arr = [int(input()) for _ in range(N)] #54321  idx: 01234


#시간초과
lst = []
for i in range(N-1, -1, -1):
    lst.append(arr[i])
print(*lst, sep='\n')


#시간초과
lst = [int(input()) for _ in range(N)]

for l in lst[::-1]:
    print(l)


#버블소트 시간초과
for i in range(1, N):  #23
    for j in range(0, N-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(*lst, sep='\n')


#카운팅소트 시간초과
#카운트
c = [0]*(N+1)   #값이 0인게 있을수도 있어서
for i in range(N):
    c[lst[i]] += 1

#누적
for i in range(1, N+1):
    c[i] += c[i-1]

#재정렬
res = [0 for _ in range(N)]   #[0]*N
for i in range(N-1, -1, -1):
    c[lst[i]] -= 1
    res[c[lst[i]]] = lst[i]
print(*res, sep='\n')

'''