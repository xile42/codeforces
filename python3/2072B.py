for _ in range(int(input())):

    n = int(input())
    s = input()
    a, b = s.count("-"), s.count("_")

    print(a // 2 * b * (a - a // 2))