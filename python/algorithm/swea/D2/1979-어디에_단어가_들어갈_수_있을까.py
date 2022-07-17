T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    rowArr = []
    colArr = []
    answer = 0
     
    for i in range(a):
        rowArr.append(list(map(int, input().split())))
    for m in range(a):
        colArr.append([])
        for n in range(a):
            colArr[m].append(rowArr[n][m])
     
    for x in range(a):
        rowCount = 0
        colCount = 0
        for y in range(a):
            if rowArr[x][y] == 1:
                rowCount += 1
            else:
                if rowCount == b:
                    answer += 1
                rowCount = 0
            if colArr[x][y] == 1:
                colCount += 1
            else:
                if colCount == b:
                    answer += 1
                colCount = 0
        if rowCount == b:
            answer += 1
        if colCount == b:
            answer += 1
    print(f"#{test_case} {answer}")