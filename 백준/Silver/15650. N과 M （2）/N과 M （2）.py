def comb(n, r, idx):
    if len(bit)==r:
        print(*bit)
        return
    else:
        for i in range(idx, n+1):  # 1 2 3 4 (1~5)
            if i not in bit:   # 조합
                bit.append(i)
                comb(n, r, i+1)
                bit.pop()
    return


n, r = map(int, input().split())
bit = []
comb(n, r, 1) #idx # 1 부터 시작