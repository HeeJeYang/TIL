T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    longArr = list(map(int, input().split()))
    shortArr = list(map(int, input().split()))
    answer = -999999
    if a < b:
        a, b = b, a
        longArr, shortArr = shortArr, longArr
    for i in range(a - b + 1):
        sum = 0
        for j in range(len(shortArr)):
            sum += longArr[i + j] * shortArr[j]
        if answer < sum:
            answer = sum
    print(f"#{test_case} {answer}")