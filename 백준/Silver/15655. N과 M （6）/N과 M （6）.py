def l_perm(perm, idx):  # 리스트가 있는 조합 
    if len(perm) == r:  # 조합은 이전꺼와 겹치면 안되므로 인덱스를 부여해준다.
        print(*perm)
        return
    else:
        for i in range(idx, n):
            #if lst[i] not in perm: # 어차피 lst의 인덱스를 욺겨주기때문에 안해줘도 됨
            perm.append(lst[i])
            l_perm(perm, i+1)
            perm.pop()



n, r = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
l_perm([], 0)