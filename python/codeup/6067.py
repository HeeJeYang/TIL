# [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)

n = int(input())

if n < 0:
    if n % 2:
        print("B")
    else:
        print("A")
else:
    if n % 2:
        print("D")
    else:
        print("C")
