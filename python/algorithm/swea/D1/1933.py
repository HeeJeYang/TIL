# 간단한 N 의 약수

T = int(input())
d = 1
while d <= T:
    if T % d == 0:
        print(d, end=" ")
    d += 1