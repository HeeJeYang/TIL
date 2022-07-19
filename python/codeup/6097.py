# [기초-리스트] 설탕과자 뽑기(py)

# 격자판 생성
h, w = map(int, input().split())
board = [["0" for _ in range(w + 1)] for _ in range(h + 1)]

# 막대의 개수 저장
n = int(input())

# 막대의 길이, 방향, 좌표를 받아 격자판에 입력
for j in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            board[x][y + i] = "1"
    else:
        for i in range(l):
            board[x + i][y] = "1"

# 격자판 출력
for row in range(1, h + 1):
    print(" ".join(board[row][1:]))
