t = int(input())
cnt = t
for t in range(t):
    input_lst = input()
    for i in range(1, len(input_lst)):
        if(input_lst[i-1] != input_lst[i] and input_lst[i] in input_lst[:i]):
            cnt -= 1
            break
print(cnt)