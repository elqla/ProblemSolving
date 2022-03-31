def ov_perm(n, r, idx):  # 중복순열
    if len(bit)==r:
        print(*bit)
        return
    else:
        for i in range(idx, n+1):
            bit.append(i)
            ov_perm(n, r, idx)
            bit.pop()
    return


n, r = map(int, input().split())
bit = []
ov_perm(n, r, 1)