# [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)

# 흰 돌의 갯수 저장
n = int(input())

# 바둑판 생성
board = [["0" for _ in range(19)] for _ in range(19)]

# 반복문으로 흰 돌의 위치 입력받아 바둑판 리스트에 저장
for i in range(n):
    x, y = map(int, input().split())

    board[x - 1][y - 1] = "1"
for i in range(19):
    print(" ".join(board[i]))
