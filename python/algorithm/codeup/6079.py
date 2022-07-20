# [기초-종합] 언제까지 더해야 할까?(py)

num = int(input())
n = 0
total = 0
while total < num:
    n += 1
    total += n
print(n)
