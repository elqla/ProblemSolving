# 9명 중 7명 구하기
lst = [int(input()) for _ in range(9)]

lst.sort()


flag = 0
for i in range(9): # 0-8
    alst = lst[:]
    alst.pop(i)
    for j in range(8): # 0-7
        blst = alst[:]
        blst.pop(j)
        if sum(blst)==100:
            flag = 1
            break
    if flag:
        break

for b in blst:
    print(b)