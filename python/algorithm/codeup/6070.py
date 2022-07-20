# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

month = int(input())

if month // 3 == 1:
    print("spring")
elif month // 3 == 2:
    print("summer")
elif month // 3 == 3:
    print("fall")
else:
    print("winter")
