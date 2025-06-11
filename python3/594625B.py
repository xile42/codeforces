from math import inf
from collections import defaultdict


for _ in range(int(input())):

    n = int(input())
    s = input()

    # if len(set(s)) == 1:
    #     print(0)
    #     continue

    d = defaultdict(lambda: defaultdict(lambda: -inf))
    dd = defaultdict(lambda: -inf)
    for i, c in enumerate(s):
        if i != n - 1:
            d[c][s[i + 1]] = max(d[c][s[i + 1]], n - i - 1)
        else:
            d[c][-1] = 0
        dd[c] = max(dd[c], n - i)

    # for k1 in d:
    #     for k2 in d[k1]:
    #         print("d[{}][{}] = {}".format(k1, k2, d[k1][k2]))
    #
    # for k in dd:
    #     print("dd[{}] = {}".format(k, dd[k]))

    ans = 0
    for c in d.keys():
        vs = d[c].values()
        if len(vs) >= 2:
            ans = max(ans, sum(sorted(vs)[-2:]))

    vs = dd.values()
    if len(vs) >= 2:
        ans = max(ans, sum(sorted(vs)[-2:]))

    print(ans)
