L = 16
notWall = ["0", "3"]
for test_case in range(1, 11):
    _ = int(input())
    dep = []
    des = []
    matrix = [list(str(input())) for row in range(L)]
    answer = "0"
    for i in range(L):
        for j in range(L):
            if matrix[i][j] == "2":
                dep = [i, j]
            if matrix[i][j] == "3":
                des = [i, j]
    storage = [dep]
    while len(storage) > 0:
        Y = storage[0][0]
        X= storage[0][1]
        if matrix[Y][X] == "3":
            answer = "1"
            break
        storage.pop(0)
        matrix[Y][X] = "4"
        if matrix[Y + 1][X] in notWall:
            storage.insert(0, [Y + 1, X])
        if matrix[Y - 1][X] in notWall:
            storage.insert(0, [Y - 1, X])
        if matrix[Y][X + 1] in notWall:
            storage.insert(0, [Y, X + 1])
        if matrix[Y][X - 1] in notWall:
            storage.insert(0, [Y, X - 1])
    print(f"#{test_case} {answer}")