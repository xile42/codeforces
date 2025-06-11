ans = 0
for _ in range(int(input())):
    if input().count("1") >= 2:
        ans += 1
print(ans)
