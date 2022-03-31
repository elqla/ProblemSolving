def dfs(idx, start, link):
    global mn
    if idx == n:
        if len(start)==len(link):
            asum = bsum = 0
            for i in range(n//2):
                for j in range(n//2):
                    asum += arr[start[i]][start[j]]
                    bsum += arr[link[i]][link[j]]
            if mn > abs(asum - bsum):
                mn = abs(asum - bsum)
        return
    dfs(idx+1, start + [idx], link)
    dfs(idx+1, start, link+[idx])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mn = 1e9
dfs(0, [], [])
# idx, start, link

print(mn)