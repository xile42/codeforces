for _ in range(int(input())):

    n = int(input())
    k = n // 15
    v = n % 15

    print(k * 3 + min(v + 1, 3))