T = int(input())
 
for test_case in range(1, T + 1):
    ans = "1"
    word = list(input())
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            ans = "0"
    print(f"#{test_case} {ans}")