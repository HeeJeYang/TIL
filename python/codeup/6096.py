# [기초-리스트] 바둑알 십자 뒤집기(py)

# 바둑판 저장
board = [list(input().split()) for _ in range(19)]
# 좌표 개수 저장
n = int(input())

# 반복문으로 좌표 지정 후 좌표 뒤집기
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if board[x - 1][j] == "1":
            board[x - 1][j] = "0"
        else:
            board[x - 1][j] = "1"

        if board[j][y - 1] == "1":
            board[j][y - 1] = "0"
        else:
            board[j][y - 1] = "1"
for i in range(19):
    print(" ".join(board[i]))
