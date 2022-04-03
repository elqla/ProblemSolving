def comb(bit, idx):
    if len(bit)==c:
        print(*bit)
    for i in range(idx, r+1):
        bit.append(i)
        comb(bit, i+1)
        bit.pop()


r, c = map(int, input().split())
comb([], 1)