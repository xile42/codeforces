from itertools import groupby


for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = 0
    for c, ite in groupby(s):
        if c == "1":
            cnt += 1

    if s[-1] == "0":
        print(2 * cnt)
    else:
        print(2 * (cnt - 1) + 1)