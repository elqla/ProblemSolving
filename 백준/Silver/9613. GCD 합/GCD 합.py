import math

t = int(input())
for _ in range(t):
	lst = list(map(int, input().split()))
	# 가능한 모든 쌍의 gcd의 합 구하기(최대공약수)
	total = 0
	for i in range(1, len(lst)):
		for j in range(i+1, len(lst)):
			total += math.gcd(lst[i], lst[j])
	print(total)