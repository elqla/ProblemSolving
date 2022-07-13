import sys, math
input = sys.stdin.readline

T = int(input())
for t in range(T):
    A, B = map(int, input().split())

    _gcd = math.gcd(A, B)  # 최대공약수

    print(A*B//_gcd)  # 최소공배수 == A*B//최대공약수