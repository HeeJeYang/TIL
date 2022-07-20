T = int(input())
#  표를 문자열로 생성
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for test_case in range(1, T + 1):

    # 문자열 저장
    input_str = input()

    for i in range(len(input_str)):
        decoded_val = table.index(input_str[i])
