import math


for _ in range(int(input())):

    s = input()
    n = int(s)
    k = math.isqrt(n)
    if k * k == n:
        print(" ".join(map(str, [0, k])))
    else:
        print(-1)
