# import sys
# sys.stdin = open('input.txt', 'r')

cnt = 0
for t in range(int(input())):
    input_lst = list(input())
    lst = [input_lst[0]]
    for i in range(1, len(input_lst)):
        if lst[i-1] == input_lst[i]:
            lst.append(input_lst[i])
        else:
            if input_lst[i] in lst:
                break
            else:
                lst.append(input_lst[i])
    if(len(input_lst)) == (len(lst)):
        cnt += 1
print(cnt)