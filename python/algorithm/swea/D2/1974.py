# 스도쿠 검증

T = int(input())
oneToNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for test_case in range(1, T + 1):
    sudoku = 1
    # 스도쿠 보드 생성
    board = []
    board1 = []
     
    for _ in range(9):
        board.append(list(map(int, input().split())))
 
    # 가로 비교
    for i in range(9):
        copyRow = board[i][:]
        copyRow.sort()
        if copyRow != oneToNine:
            sudoku = 0
     
    # 세로 비교
    for i in range(9):
        copyCol = []
        for j in range(9):
            copyCol.append(board[j][i])
        copyCol.sort()
        if copyCol != oneToNine:
            sudoku = 0
    for i in range(0, 9, 3):
        squareOne = board[0 + i][0:3] + board[1 + i][0:3] + board[2 + i][0:3]
        squareTwo = board[0 + i][3:6] + board[1 + i][3:6] + board[2 + i][3:6]
        squareThree = board[0 + i][6:9] + board[1 + i][6:9] + board[2 + i][6:9]
        squareOne.sort()
        squareTwo.sort()
        squareThree.sort()
        if squareOne != oneToNine or squareTwo != oneToNine or squareThree != oneToNine:
            sudoku = 0
    print(f"#{test_case} {sudoku}")