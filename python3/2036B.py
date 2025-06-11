from collections import Counter


for _ in range(int(input())):
    n, k = list(map(int, input().split(" ")))
    cnt = Counter()
    for _ in range(k):
        b, c = input().split(" ")
        cnt[b] += int(c)
    print(sum(sorted(cnt.values(), reverse=True)[:n]))

