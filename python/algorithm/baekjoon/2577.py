# 입력받은 세 개의 숫자를 곱해줄 변수
mul_num = 1

# 0~9의 숫자가 몇 번 쓰였는지 알려줄 리스트
numbers = [0 for _ in range(10)]

# 숫자 세 개 입력받음
for i in range(3):
    mul_num *= int(input())

# 문자열로 변환
mul_num = str(mul_num)

# 각 숫자와 인덱스가 일치하는 값에 1을 더함
for i in mul_num:
    numbers[int(i)] += 1

# 출력
print(*numbers, sep="\n")
