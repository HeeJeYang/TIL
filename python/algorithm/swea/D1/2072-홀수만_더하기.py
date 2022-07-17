T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    answer = 0
    for number in numbers:
        if number % 2:
            answer += number
    print(f"#{test_case} {answer}")