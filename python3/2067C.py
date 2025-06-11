for _ in range(int(input())):

    sn = input()
    n = int(sn)

    if "7" in sn:
        print(0)
        continue

    for i in range(1, 8):
        k = n - i
        sk = str(k)
        if len(sk) < len(sn):
            sk = "0" + sk
        ans = float("inf")
        for c in sk:
            v = (ord(c) - ord("0"))
            if v <= 7:
                ans = min(ans, 7 - v)
            else:
                ans = min(ans, 17 - v)

        if ans <= i:
            print(i)
            break
    else:
        print(7)
