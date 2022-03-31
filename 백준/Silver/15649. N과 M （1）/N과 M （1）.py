def perm(n, r, idx):
    if len(bit) == r:
        print(*bit)
    else:
        for i in range(1, n+1):
            if i not in bit:
                bit.append(i)
                perm(n, r, idx+1)
                bit.pop()
    return


n, r = map(int, input().split())

bit = []
res = perm(n, r, 1)