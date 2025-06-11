for _ in range(int(input())):

    n, m, k = list(map(int, input().split(" ")))  # n 0, m 1

    if n < k and m < k:
        print(-1)
        continue

    ans = str()
    cn = "0"
    cm = "1"
    if n <= m:
        n, m = m, n
        cn, cm = cm, cn

    round = 0  # n 0, m 1
    pre = float("inf")
    while (round == 0 and n > 0) or (round == 1 and m > 0):
        v = min(pre, k, n if round == 0 else m)
        ans += (cn if round == 0 else cm) * v
        if round == 0:
            n -= v
        else:
            m -= v
        round = 1 - round
        pre = v

    if m or n:
        print(-1)
    else:
        print(ans)