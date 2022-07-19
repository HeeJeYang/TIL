# [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)

n = int(input())
clap = [3, 6, 9]

for i in range(1, n + 1):
    if i % 10 in clap:
        print("X", end=' ')
    else:
        print(i, end=' ')
