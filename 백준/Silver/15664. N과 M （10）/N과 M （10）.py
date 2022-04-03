def comb(bit, idx):
    if len(bit)==c:
        print(*bit)

    tmp = 0
    for i in range(idx, r):
        if tmp != lst[i]:
            bit.append(lst[i])
            tmp = lst[i]
            comb(bit, i+1)
            bit.pop()


r, c = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
comb([], 0)