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


n = int(input())
g = [[] for _ in range(n + 1)]
ps = list(map(int, input().split()))
cs = [0] + list(map(int, input().split()))

for i, v in enumerate(ps):
    u = i + 2
    g[u].append(v)
    g[v].append(u)

ans = 0
vis = [False] * (n + 1)
q = deque([(1, 0)])

while q:

    i, c = q.popleft()
    vis[i] = True
    if cs[i] != c:
        ans += 1
    cur = cs[i]

    for j in g[i]:
        if vis[j]:
            continue
        q.append((j, cur))

print(ans)
