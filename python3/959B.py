from math import *
from typing import *
from collections import *
from random import randrange


"""
codeforces-python: 算法竞赛Python3模板库
#1: Python int 随机异或, 对抗哈希攻击
https://github.com/xile42/codeforces-python/blob/main/templates/safe.py
"""
RANDOM_KEY = randrange(1 << 29)  # 2 ^ 29: 避免生成的随机数超出普通整数范围, 避免大整数运算, 提高性能; 不同版本(pypy/python3, 32bit/64bit)这个范围不同, 2 ^ 29是通用保险范围

def XorRandomly(x: int) -> int:
    return x ^ RANDOM_KEY


n, k, m = map(int, input().split())
words = input().split()
idx_map = {w: i for i, w in enumerate(words)}
costs = list(map(int, input().split()))

root = dict()
cost_of_root = defaultdict(lambda: inf)

for ki in range(k):
    ns = list(map(int, input().split()))
    for i in range(1, len(ns)):
        root[ns[i] - 1] = ki
        cost_of_root[ki] = min(cost_of_root[ki], costs[ns[i] - 1])

s = input().split()
ans = 0
for w in s:
    ans += cost_of_root[root[idx_map[w]]]

print(ans)
