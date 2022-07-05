a, b = map(int, input().split())

#최대공약수 구하기
#두수를나눌때 가장 마지막으로 큰 수로 나누어 떨어지는 수
mx = 1
mn_num = min(a, b)
while mn_num:
    if a%mn_num == 0 and b%mn_num == 0:
        mx = mn_num
        break
    else:
        mn_num -= 1
print(mx)

#최소공배수 구하기
#두수에서 서로소가 나올때까지 작은수로 나눠준다.
lst = [] #곱할값 모으기
mn = 1
x = 2
while x <= min(a, b):
    if a%x == 0 and b%x == 0:
        a, b = a//x, b//x
        lst.append(x)
        x = 2
    else:
        x += 1
lst.extend([a, b])

if lst:
    answer = 1
    for x in lst:
        answer*=x
    print(answer)
else:
    print(1)
