n = int(input())
lst = [input() for _ in range(n)]


#중복제거
new_lst = list(set(lst))

# 알파벳순 정렬
new_lst.sort()

# 길이순정렬
new_lst.sort(key = len)

for i in new_lst:
    print(i)

