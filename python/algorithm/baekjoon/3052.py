# 나머지

# 서로 다른 값
answer = set()

for i in range(10):
    answer.add(int(input()) % 42)

# 서로 다른 값의 개수 출력
print(len(answer))
