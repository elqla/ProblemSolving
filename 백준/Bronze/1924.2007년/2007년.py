il = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


x, y = map(int, input().split())
wal = 0
for i in range(x - 1):  # 1월이면, 31일까지 안감/if 2.8 = 31+8
    wal += il[i]  # 월 만큼 추가.. 요일은 day다 더해서 /7 하면 나옴
res = (wal + y) % 7
print(day[res])
