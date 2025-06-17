from random import randrange
from collections import Counter


"""
codeforces-python: 算法竞赛Python3模板库
#1: Python int 随机异或, 对抗哈希攻击
https://github.com/xile42/codeforces-python/blob/main/templates/safe.py
"""
RANDOM_KEY = randrange(1 << 29)  # 2 ^ 29: 避免生成的随机数超出普通整数范围, 避免大整数运算, 提高性能; 不同版本(pypy/python3, 32bit/64bit)这个范围不同, 2 ^ 29是通用保险范围

def XorRandomly(x: int) -> int:
    return x ^ RANDOM_KEY


for _ in range(int(input())):

    n = int(input())
    s = input()

    c = Counter(s)
    c[s[0]] -= 1
    c[s[-1]] -= 1

    if max(c.values()) > 1:
        print("YES")
        continue

    if c[s[0]] > 0 or c[s[-1]] > 0:
        print("YES")
        continue

    print("NO")
