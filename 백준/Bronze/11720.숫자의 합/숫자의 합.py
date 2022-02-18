l = int(input())
word = list(map(int, input()))
cnt = 0
for i in range(l):
    cnt += word[i]
print(cnt)