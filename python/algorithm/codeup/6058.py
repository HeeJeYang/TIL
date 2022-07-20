# [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)

a, b = map(bool, map(int, input().split()))

print((not a) and (not b))