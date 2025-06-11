from bisect import bisect_left


for _ in range(int(input())):
    n, m = list(map(int, input().split(" ")))
    ns = list(map(int, input().split(" ")))
    ms = list(map(int, input().split(" ")))

    ms.sort()
    pre = min(ns[0], ms[0] - ns[0])
    success = True
    # print(pre)
    for _, cur in enumerate(ns[1:]):
        v1 = cur
        target = pre + cur
        idx = bisect_left(ms, target)
        v2 = -float("inf") if idx == m else ms[idx] - cur
        # print(pre, v1, v2)
        if v1 > v2:
            v1, v2 = v2, v1
        if v1 >= pre:
            v = v1
        elif v2 >= pre:
            v = v2
        else:
            success = False
            break
        pre = v

    print("YES" if success else "NO")