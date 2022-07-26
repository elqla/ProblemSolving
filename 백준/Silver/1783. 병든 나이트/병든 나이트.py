N, M = map(int, input().split())
# 세로 가로
# 세로는  3이상이면서, 가로가 7이상이면 모든 경우를 다 쓸 수 있음
# 그러나 가로가 6 이하면 최대 4칸만 갈 수 있음

all_res = 5
if N==1:
	print(1)
elif N==2:
	print(min(4, (M-1)//2 + 1))
elif M<=6:
	print(min(4, M))
else:
	print(M-2)