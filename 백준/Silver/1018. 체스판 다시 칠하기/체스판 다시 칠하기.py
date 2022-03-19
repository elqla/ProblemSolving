n, m = map(int, input().split())

# mmm n
# mmm n
arr = [list(map(str, input())) for _ in range(n)]
repair = []

# 보드의 첫 시작이 W이면
for i in range(n-7):
    for j in range(m-7):
        first_w = 0  # first가 white로 시작할 때
        first_b = 0  # first가 black으로 시작할 때
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:  # 인덱스 합이 짝수일때
                    if arr[k][l] != 'W':
                        first_w = first_w + 1
                        # 보드의 첫 시작이, B이면
                    if arr[k][l] != 'B':
                        first_b = first_b + 1
                else: # 인덱스의 합이 홀수일때,
                    if arr[k][l] != 'B':
                        first_w = first_w + 1
                    if arr[k][l] != 'W':
                        first_b = first_b + 1
        # 하나의 8x8배열을 돌았을때,
        # w로 시작할때와, b로 시작할때를 고려한 값을 저장해준다.
        repair.append(first_w)
        repair.append(first_b)
print(min(repair))

# WBWB
# BWBW
# WBWB

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23

# k + l = 짝수(00, 02, 11, 13...)가 start 지점의 값을 가짐
# 따라서, W로 시작해야하는데, W로 시작하지 않을 시
# first_w에 +1 을 해주고, k+l이 홀수 인덱스를 가지는 곳에선 B여야 하는데
# 만약 B가 아닐경우 역시 first_w의 인덱스를 증가시킨다.