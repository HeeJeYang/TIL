# [기초-종합] 수 나열하기3(py)

a, m, d, n = map(int, input().split())

ans = a

for i in range(2, n + 1):
    ans = ans * m + d

print(ans)
