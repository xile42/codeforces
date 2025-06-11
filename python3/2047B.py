from collections import Counter


for _ in range(int(input())):
    l = int(input())
    w = input()
    c = Counter(w)
    if len(c.keys()) == 1:
        print(w)
    else:
        kvs = sorted(c.items(), key=lambda x: x[-1])
        a, b = kvs[0][0], kvs[-1][0]
        print(w.replace(a, b, 1))
