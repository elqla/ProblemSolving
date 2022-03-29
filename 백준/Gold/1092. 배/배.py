import sys
input = sys.stdin.readline
# 크레인 및 무게
n = int(input())
kr = list(map(int, input().split()))

# 박스 개수 및 무게
m = int(input())
box = list(map(int, input().split()))



res = 0
kr.sort(reverse=True)
box.sort(reverse=True)

time = 0
if max(box)>max(kr):
    time = -1
else:
    while box:
        for k in kr:
            for b in box:
                if k>=b:
                    box.remove(b)
                    break
                    # 박스를 뽑고 다음 크레인으로 넘어감
                    # 계속 크레인보다 작은 박스를 찾아서 없앰
        time += 1
print(time)
