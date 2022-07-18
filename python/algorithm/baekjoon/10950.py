# A+B-3

# 테스트 케이스의 개수 저장
T = int(input())

# 각 테스트 케이스
for test_case in range(T):
    # 두 정수 A, B 저장
    A, B = map(int, input().split())
    # A + B 출력
    print(A + B)
