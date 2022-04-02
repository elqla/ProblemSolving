def l_perm(perm):
    if len(perm) == r:
        print(*perm)
        return  # 함수 내부에서, 하나 하나 호출되면서 perm값이 계속 변경되는데, 이 값을 밖의 리스트에 어팬드 할 수 없다.

    last = 0  # [1, 7 에서 7 저장하고, 1, 9에서 9를 저장하면, 다음 9가 올때 이미 9가 있으므로 다음자리에 올 수 없음]
    for i in range(n):  # last는 for문을 돌면서계속 새로운 값을 저장해줄 수 있어서 초기화 되지 않고, 두번째 값을 계속 저장할 수 있다.
        if is_used[i]==True: continue
        if last == lst[i]: continue

        is_used[i] = True
        perm.append(lst[i])
        last = lst[i]
        l_perm(perm)
        is_used[i] = False
        perm.pop()

n, r = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort() # 1 7 9 9
is_used = [False for _ in range(n)]
l_perm([])

'''
4 2
9 7 9 1
'''