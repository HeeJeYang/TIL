T = int(input())
for test_case in range(1, T + 1):
    L = int(input())
    matrix = [list(map(int, input().split())) for i in range(L)]
    answer = ["" for _ in range(L)]
    for _ in range(3):
        matrix = [[row[i] for row in matrix[::-1]] for i in range(L)]
        copyMatrix = ["".join(map(str, matrix[row])) for row in range(L)]
        answer = [answer[i] + " " + copyMatrix[i] for i in range(L)]
    answer = [answer[row][1:] for row in range(L)]
    print(f"#{test_case}")
    print("\n".join(answer))