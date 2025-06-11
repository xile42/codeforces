from collections import Counter


for _ in range(int(input())):

    n = int(input())
    ns = list(map(int, input().split(" ")))

    c = Counter(ns)
    ks = sorted(c.keys())
    success = True
    while ks:
        k = ks[0]
        v = c[k]
        ks = ks[1:]
        if v == 1:
            success = False
            break
        else:
            c[k + 1] += v - 2
            if v > 2 and (not ks or ks[0] != k + 1):
                ks = [k + 1] + ks

    print("YES" if success else "NO")