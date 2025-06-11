for _ in range(int(input())):
    ans = 0
    wc, size = map(int, input().split(" "))
    flag = True
    for _ in range(wc):
        w = input()
        l = len(w)
        if flag and size >= l:
            ans += 1
            size -= l
        else:
            flag = False
            continue

    print(ans)
