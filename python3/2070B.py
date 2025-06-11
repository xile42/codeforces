for _ in range(int(input())):

    n, x, k = list(map(int, input().split(" ")))
    s = input()

    cur = x
    i = 0
    ans = 0
    first = second = None

    stop = False
    for t in range(1, k + 1):
        cur += 1 if s[i] == "R" else -1
        if cur == 0:
            i = 0
            ans += 1
            if first is None:
                first = t
            else:
                second = t
                break
        else:
            i += 1
            if i >= n:
                stop = True
                break

    if stop:
        print(ans)
    elif first and second:
        print(1 + (k - first) // (second - first))
    else:
        print(ans)