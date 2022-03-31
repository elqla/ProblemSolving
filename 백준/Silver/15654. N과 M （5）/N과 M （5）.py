def l_perm(perm):  # 리스트가 있는 순열
    if len(perm) == r:
        print(*perm)
    else:
        for l in lst:
            if l not in perm:
                perm.append(l)
                l_perm(perm)
                perm.pop()
    return


n, r = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
l_perm([])