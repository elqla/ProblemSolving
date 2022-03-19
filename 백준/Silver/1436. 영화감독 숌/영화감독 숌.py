# n번째 영화의 제목 = n번째로 작은 종말의 숫자
# 666을 포함하는 숫자 중, 몇번째의 숫자를 인풋받음
# 몇번재에 해당하는 수 출력


# 1// 0666
# 2// 1666


n = int(input()) # 몇번째인지 알기 위함
movie = 0 # 일반 숫자 1부터 ~
cnt = 0 # cnt와 n이 일치할때,
while 1:
    if '666'in str(movie):
        cnt += 1
    if n == cnt:
        print(movie)
        break
    movie += 1