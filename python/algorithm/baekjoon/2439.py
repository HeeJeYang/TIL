# 별 찍기 - 2

T = int(input())

for i in range(T):
    row = ""
    for j in range(T):
        if i + j >= T - 1:
            row += "*"
        else:
            row += " "
    print(row)
