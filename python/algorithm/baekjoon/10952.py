# A + B - 5

# A, B 선언
A = -1
B = -1

while True:
    A, B = map(int, input().split())
    # A, B가 모두 0일 때 종료
    if A == 0 and B == 0:
        break
    print(A + B)
