# 최댓값

import sys

max_num = {}
for i in range(1, 10):

    # 숫자 입력 받음
    num = int(sys.stdin.readline())

    # max_num이 비어있으면 idx, num 추가
    if len(max_num) == 0:
        max_num['idx'] = i
        max_num['num'] = num

    # 기존의 최댓값과 비교하여 새로운 값이 더 크면 교체
    else:
        if max_num['num'] < num:
            max_num['idx'], max_num['num'] = i, num

# 가장 큰 숫자와 인덱스 출력
print(max_num['num'])
print(max_num['idx'])
