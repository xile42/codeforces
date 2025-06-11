x = 0
for _ in range(int(input())):
    s = input()
    x += 1 if "+" in s else -1

print(x)
