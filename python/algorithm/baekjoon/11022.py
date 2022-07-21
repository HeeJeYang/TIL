# A+B-8

import sys

# 테스트 케이스 입력 받아 저장
T = int(sys.stdin.readline())

for test_case in range(1, T + 1):

    A, B = map(int, sys.stdin.readline().split())

    # 출력
    print(f'Case #{test_case}: {A} + {B} = {A + B} ')
