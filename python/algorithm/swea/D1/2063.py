# 중간값 찾기

a = int(input())
b = list(map(int, input().split()))
b.sort()
print(b[a // 2])