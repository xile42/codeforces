for _ in range(int(input())):

    x = int(input())
    sx = bin(x)[2:]
    l = len(sx)
    sx = "0" * (30 - l) + sx

    ans = list()
    ans.append(x)
    for i in range(1, 31):
        c = sx[-i]
        if c == "0":
            sv = sx[:-i] + "1" if i == 1 else sx[:-i] + "1" + sx[-(i - 1):]
            v = int(sv, 2)
            ans.append(v)

    print(len(ans))
    print(" ".join(list(map(str, ans))))
