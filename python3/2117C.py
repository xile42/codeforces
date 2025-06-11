from random import randrange
from collections import Counter


"""
codeforces-python: 算法竞赛Python3模板库
#1: Python int 随机异或, 对抗哈希攻击
https://github.com/xile42/codeforces-python/blob/main/templates/safe.py
"""
RANDOM_KEY = randrange(1 << 29)  # 2 ^ 29: 避免生成的随机数超出普通整数范围, 避免大整数运算, 提高性能; 不同版本(pypy/python3, 32bit/64bit)这个范围不同, 2 ^ 29是通用保险范围

def XorRandomly(x):
    return x ^ RANDOM_KEY


for _ in range(int(input())):

    n = int(input())
    ns = list(map(XorRandomly, map(int, input().split())))
    c = Counter(ns)

    ans = 1
    need = set()
    satisfied = set()
    for v in ns:
        if c[v] == 1:
            break
        need.add(v)
        if v in satisfied:
            satisfied.remove(v)
        if len(satisfied) == 0:
            ans += 1
            satisfied = need.copy()
        c[v] -= 1

    print(ans)