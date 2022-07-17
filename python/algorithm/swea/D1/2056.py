# 연월일 달력

T = int(input())
for test_case in range(1, T + 1):
    date = input()
    month = int(date[4:6])
    day = int(date[6:])
    if (month == 0 or month > 12) or (month == 2 and day > 28) or (((month < 8 and month % 2) or (month >= 8 and month % 2 == 0)) and day > 31) or (((month < 8 and month % 2 == 0) or (month > 8 and month % 2)) and day > 30):
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {date[0:4]}/{date[4:6]}/{date[6:]}")