# 알파벳을 숫자로 변환

s = list(input())
s = [str(ord(s[a]) - 64) for a in range(len(s))]
print(" ".join(s))