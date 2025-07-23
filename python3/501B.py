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
known = dict()
ans = 0
for _ in range(n):
    old, new = input().split()
    if old not in known:
        known[new] = old
        ans += 1
    else:
        known[new] = known[old]
        del known[old]

print(len(known))
for new, old in known.items():
    print(" ".join([old, new]))
