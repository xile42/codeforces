for _ in range(int(input())):

    ns = list(map(int, input().split(" ")))

    print("YES" if len(set(ns)) == 1 else "NO")
