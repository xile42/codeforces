for _ in range(int(input())):

    x, y = list(map(int, input().split(" ")))
    if x + 1 == y or (x > y and (x - (y - 1)) % 9 == 0):
        print("YES")
    else:
        print("NO")