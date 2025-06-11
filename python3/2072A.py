from math import ceil


for _ in range(int(input())):

    n, k, p = list(map(int, input().split(" ")))
    if k > n * p or k < -n * p:
        print(-1)
        continue

    ans = ceil(abs(k) / p)
    print(ans)