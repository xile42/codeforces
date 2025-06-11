from heapq import *


for _ in range(int(input())):
    n = int(input())
    ns = list(map(int, input().split(" ")))
    if n == 1:
        print(ns[0])
        continue
    heapify(ns)
    while len(ns) >= 2:
        a = heappop(ns)
        b = heappop(ns)
        heappush(ns, a + b - 1)

    print(ns[0])