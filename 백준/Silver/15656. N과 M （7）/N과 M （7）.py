def ov_l_perm(perm):  # 리스트가 있는 중복 순열
    if len(perm) == r:
        print(*perm)
        return
    else:
        for i in range(n):
            #if lst[i] not in perm:
            perm.append(lst[i])
            ov_l_perm(perm)
            perm.pop()



n, r = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ov_l_perm([])