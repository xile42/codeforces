for _ in range(int(input())):

    n = int(input())

    ans = list(range(1, n + 1, 2)) + list(range(2, n + 1, 2)[::-1])

    print(" ".join(map(str, ans)))
