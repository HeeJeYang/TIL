# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())

for i in range(1, T + 1):
    test_case = int(input())

    # 수학 성적 리스트에 저장한 뒤 내림차순
    math_score = sorted(list(map(int, input().split())), reverse=True)

    # [최빈수, 개수] 초기 저장
    mode = [math_score[0], 1]

    # 반복문 돌 때 개수 세는 변수 저장
    n = 1

    for i, v in enumerate(math_score):
        # 이전 값과 점수가 다를 경우 현재 최빈수 개수와 비교하여 더 클 경우 최빈수 교체
        if v != math_score[i - 1]:
            if n > mode[1]:
                mode[0] = math_score[i - 1]
                mode[1] = n
            n = 1
        # 이전 값과 점수가 같을 경우 개수 + 1
        else:
            n += 1
    # 마지막 값 검사하기
    else:
        if n > mode[1]:
            mode[0] = math_score[999]
            mode[1] = n

    # 최빈수 값 출력
    print(f"#{test_case} {mode[0]}")
