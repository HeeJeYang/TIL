# 오븐 시계

hour, minute = map(int, input().split())
minute += int(input())

while minute >= 60:
    hour += 1
    minute -= 60
while hour >= 24:
    hour -= 24

print(f"{hour} {minute}")