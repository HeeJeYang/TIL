# A+B-7

import sys

# 테스트 케이스의 개수 저장
T = int(sys.stdin.readline())

# 각 테스트 케이스
for test_case in range(1, T + 1):

    # 두 정수 A, B 값 저장
    A, B = map(int, sys.stdin.readline().split())

    # A + B 출력
    print(f"Case #{test_case}: {A + B}")
