# Base64 Decoder

T = int(input())
#  표를 문자열로 생성
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for test_case in range(1, T + 1):

    # 문자열 저장
    input_str = input()
    decoded_val = ""
    answer = ""

    # decoding한 값 decoded_val에 추가
    for i in range(len(input_str)):
        val = bin(table.index(input_str[i]))[2:]

        # val의 길이가 6보다 적을 경우, val 앞에 '0' 추가를 반복
        while len(val) < 6:
            val = "0" + val

        decoded_val += val

    # 1바이트씩 끊어서 아스키 코드로 변환
    while len(decoded_val) > 0:
        answer += chr(int("0b" + decoded_val[:8], 2))
        decoded_val = decoded_val[8:]

    print(f"#{test_case} {answer}")
