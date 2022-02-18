n = int(input())
for i in range(1, n):  #2*(n-i)
    print('*'*i + ' '*(2*(n-i)) + '*'*i)
for i in range(n, 0, -1):
    print('*'*i + ' '*(2*(n-i)) + '*'*i)