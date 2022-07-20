# [기초-종합] 16진수 구구단 출력하기(py)

n = int(input(), 16)
cnt = 16

for i in range(1, cnt):
    print("%X*%X=%X" % (n, i, n * i))
