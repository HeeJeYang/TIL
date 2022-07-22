# 최소, 최대

import sys

# 정수의 개수 N 저장
N = int(sys.stdin.readline())

# N개의 정수 리스트에 저장
numbers = list(map(int, sys.stdin.readline().split()))

print(min(numbers), max(numbers))
