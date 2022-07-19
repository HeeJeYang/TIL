# [기초-리스트] 성실한 개미(py)

# 미로판 저장
maze = []
for row in range(10):
    maze.append(list(input().split()))

# 개미집 좌표 (2 - 1, 2 - 1)
X = 1
Y = 1
while maze[Y][X] != "2":

    # 개미 위치의 값을 "9"로 변환
    maze[Y][X] = "9"

    # 오른쪽이 갈 수 있는 곳이면 이동
    if maze[Y][X + 1] != "1":
        X += 1

    # 아닐 시 아래가 갈 수 있는 곳이면 이동
    elif maze[Y + 1][X] != "1":
        Y += 1

    # 아닐 시 정지
    else:
        break

# 현재 위치 "9"로 변환
maze[Y][X] = "9"

# 미로판 출력
for row in range(10):
    print((" ".join(maze[row])))
