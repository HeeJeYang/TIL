# 더하기 사이클

N = int(input())
save_new_number = N
new_number = -1
count = 0
while N != new_number:
    count += 1
    sum_of_digit = save_new_number // 10 + save_new_number % 10
    save_new_number = new_number = sum_of_digit % 10 + (save_new_number % 10) * 10

print(count)
