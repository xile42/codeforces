from itertools import accumulate

for _ in range(int(input())):
    n, m = list(map(int, input().split(" ")))

    arr = list()
    for _ in range(n):
        ns = list(map(int, input().split(" ")))
        acc = list(accumulate(ns))
        arr.append([acc[-1], sum(acc)])

    arr.sort(reverse=True)
    ans = 0
    for idx, (arr_sum, arr_acc) in enumerate(arr):
        ans += arr_acc
        ans += arr_sum * (len(arr) - idx - 1) * m

    print(ans)