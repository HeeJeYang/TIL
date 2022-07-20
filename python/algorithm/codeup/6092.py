# [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)

from random import random


n = int(input())

randomList = list(map(int, input().split()))
attendance = [0 for _ in range(23)]

for i in randomList:
    attendance[i - 1] += 1
for i in attendance:
    print(i, end=" ")
