# 알람 시계

hour, minute = map(int, input().split())

if minute < 45:
    if hour == 0:
        hour = 23
    else:
        hour -= 1
    minute += 60

print(f"{hour} {minute - 45}")
