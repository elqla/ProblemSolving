lst = list(input())
res_lst = []
for i in range(len(lst)):
	res_lst.append(''.join(lst[i:]))
print('\n'.join(sorted(res_lst)))