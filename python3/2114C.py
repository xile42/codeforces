for _ in range(int(input())):

    n = int(input())
    ns = list(map(int, input().split()))

    ans = 1
    cur = ns[0] + 2
    for v in ns[1:]:
        if v >= cur:
            ans += 1
            cur = v + 2

    print(ans)
