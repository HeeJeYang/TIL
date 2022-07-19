# [기초-종합] 짝수 합 구하기(설명)(py)

n = int(input())

t = [i for i in range(n + 1) if i % 2 == 0]

print(sum(t))
