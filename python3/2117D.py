for _ in range(int(input())):

    n = int(input())
    ns = list(map(int, input().split()))

    v = 2 * ns[0] - ns[1]
    if v % (n + 1) != 0:
        print("NO")
        # print("%(n+1) 退出")
        continue

    b = v // (n + 1)
    a = ns[0] - n * b
    # print(a, b)

    if a < 0 or b < 0:
        print("NO")
        continue

    for i in range(2, n):
        cur = ns[i]
        expect = a * (i + 1) + b * (n - (i + 1) + 1)
        if cur != expect:
            print("NO")
            # print("i: {}, cur: {}, expect: {}".format(i, cur, expect))
            break
    else:
        print("YES")
