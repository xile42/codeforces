a, b = map(int, input().split(" "))
c = {1, 2, 3} - {a, b}
print(list(c)[0])
