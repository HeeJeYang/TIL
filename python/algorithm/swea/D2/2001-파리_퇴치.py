T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    sumVal = 0
    answer = 0
    for row in range(N):
        matrix.append(list(map(int, input().split())))
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            isMaximum = 0
            for k in range(M):
                isMaximum += sum(matrix[i + k][j:j + M])
            answer = answer if isMaximum < answer else isMaximum
    print(f"#{test_case} {answer}")