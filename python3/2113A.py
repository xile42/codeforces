from math import ceil, inf
from random import randrange

"""
codeforces-python: 算法竞赛Python3模板库
#1: Python int 随机异或, 对抗哈希攻击
https://github.com/xile42/codeforces-python/blob/main/templates/safe.py
"""
RANDOM_KEY = randrange(1 << 29)  # 2 ^ 29: 避免生成的随机数超出普通整数范围, 避免大整数运算, 提高性能; 不同版本(pypy/python3, 32bit/64bit)这个范围不同, 2 ^ 29是通用保险范围


def XorRandomly(x: int) -> int:
    return x ^ RANDOM_KEY


for _ in range(int(input())):

    k, a, b, x, y = map(int, input().split())

    ans1 = 0
    cur = k

    if cur >= a:
        diff = max(0, cur - a)
        cnt = ceil(diff / x) if diff % x != 0 else ceil(diff / x) + 1
        ans1 += cnt
        cur -= cnt * x
        # print(cur, ans1, cnt)

    if cur >= b:
        diff = max(0, cur - b)
        cnt = ceil(diff / y) if diff % y != 0 else ceil(diff / y) + 1
        ans1 += cnt
        cur -= cnt * y
        # print(cur, ans1, cnt)

    ans2 = 0
    cur = k

    if cur >= b:
        diff = max(0, cur - b)
        cnt = ceil(diff / y) if diff % y != 0 else ceil(diff / y) + 1
        ans2 += cnt
        cur -= cnt * y
        # print(cur, ans2, cnt)

    if cur >= a:
        diff = max(0, cur - a)
        cnt = ceil(diff / x) if diff % x != 0 else ceil(diff / x) + 1
        ans2 += cnt
        cur -= cnt * x
        # print(cur, ans2, cnt)

    print(max(ans1, ans2))
