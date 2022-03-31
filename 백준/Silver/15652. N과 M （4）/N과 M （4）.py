def ov_comb(n, r, idx):  # 중복조합
    if len(bit)==r:
        print(*bit)
        return
    else:
        for i in range(idx, n+1):
            bit.append(i)
            ov_comb(n, r, i)
            bit.pop()
    return


n, r = map(int, input().split())
bit = []
ov_comb(n, r, 1)