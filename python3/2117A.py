for _ in range(int(input())):

    n, x = map(int, input().split())
    ns = list(map(int, input().split()))

    need = 0
    pre = None
    for i, v in enumerate(ns):
        if v == 1:
            if pre is None:
                pre = i
                continue
            else:
                need = max(need, i - pre + 1)
                continue

    if need <= x:
        print("YES")
    else:
        print("NO")
