import sys
while True:
		lst = sys.stdin.readline().rstrip('\n')
		if not lst:
			break
		low = up = num = none = 0

		for l in lst:
			if l.isupper():
					up += 1
			elif l.islower():
				low += 1
			elif l.isdigit():
				num += 1
			else:
				none += 1
		print(low, up, num, none)