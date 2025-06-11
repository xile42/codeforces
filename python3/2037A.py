from collections import Counter


for _ in range(int(input())):
    n = int(input())
    ns = list(map(int, input().split(" ")))
    ans = 0
    for k, v in Counter(ns).items():
        ans += v // 2
    print(ans)
