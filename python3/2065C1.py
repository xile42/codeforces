for _ in range(int(input())):
    n, m = list(map(int, input().split(" ")))
    ns = list(map(int, input().split(" ")))
    k = int(input())

    arr = list()
    for v in ns:
        other = k - v
        if v <= other:
            arr.append([v, other])
        else:
            arr.append([other, v])

    cur = arr[0][0]
    success = True
    for a, b in arr[1:]:
        if cur <= a:
            cur = a
            continue
        elif cur <= b:
            cur = b
            continue
        else:
            success = False

    print("YES" if success else "NO")