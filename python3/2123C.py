from math import inf
from random import randrange


"""
codeforces-python: 算法竞赛Python3模板库
#1: Python int 随机异或, 对抗哈希攻击
https://github.com/xile42/codeforces-python/blob/main/templates/safe.py
"""
RANDOM_KEY = randrange(1 << 29)  # 2 ^ 29: 避免生成的随机数超出普通整数范围, 避免大整数运算, 提高性能; 不同版本(pypy/python3, 32bit/64bit)这个范围不同, 2 ^ 29是通用保险范围

def XorRandomly(x: int) -> int:
    return x ^ RANDOM_KEY


min = lambda x, y: x if x < y else y
max = lambda x, y: x if x > y else y


for _ in range(int(input())):

    n = int(input())
    ns = list(map(int, input().split()))

    ans = list()

    pre = [inf] * n
    pre[0] = ns[0]
    for i in range(1, n):
        pre[i] = min(pre[i - 1], ns[i])

    suf = [-inf] * n
    suf[-1] = ns[-1]
    for i in range(n - 2, -1, -1):
        suf[i] = max(suf[i + 1], ns[i])

    for i, v in enumerate(ns):
        if i == 0 or i == n - 1:
            ans.append("1")
            continue
        if pre[i - 1] < v < suf[i + 1]:
            ans.append("0")
        else:
            ans.append("1")

    print("".join(ans))
