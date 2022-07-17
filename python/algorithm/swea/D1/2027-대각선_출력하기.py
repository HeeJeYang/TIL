for i in range(5):
    ans = ""
    for j in range(5):
        if i == j:
            ans += "#"
        else:
            ans += "+"
    print(ans)
            