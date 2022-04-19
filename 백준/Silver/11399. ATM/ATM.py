# 인출시간이 작은것부터 sort
# 어차피 최소합구하는 것이므로
n = int(input())
time = list(map(int, input().split()))
time.sort()
for i in range(1, n):
    time[i] += time[i-1]
print(sum(time))
