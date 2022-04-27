E, S, M = map(int, input().split())



x, y, z = 0, 0, 0
year = 0
while 1:
    year += 1
    x += 1
    y += 1
    z += 1


    if x==E and y==S and M==z:
        print(year)
        break
    if x==15:
        x = 0
    if y==28:
        y = 0
    if z==19:
        z = 0