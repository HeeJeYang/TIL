# 빠른 A+B

import sys

# 테스트 케이스의 개수 저장
T = int(sys.stdin.readline())

# A, B 값 저장한 뒤 A + B 출력
for test_case in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
