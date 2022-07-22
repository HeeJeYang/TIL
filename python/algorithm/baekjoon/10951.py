# A + B - 4
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    # 오류 시 while문 탈출
    except:
        break
