# 큰 놈, 작은 놈, 같은 놈

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    ans = ""
    if a < b:
        ans += "<"
    elif a > b:
        ans += ">"
    else:
        ans += "="
    print(f"#{test_case} {ans}")