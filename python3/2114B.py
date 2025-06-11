from collections import Counter


for _ in range(int(input())):

    l, k = map(int, input().split())
    s = input()

    n = l // 2
    c = Counter(s)
    c0, c1 = c["0"], c["1"]

    if c0 >= n - k and c1 >= n - k and not c0 - (n - k) & 1 and not c1 - (n - k) & 1:
        print("YES")
    else:
        print("NO")
