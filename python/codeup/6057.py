# [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)

a, b = map(bool, map(int, input().split()))
print((a and b) or ((not a) and (not b)))