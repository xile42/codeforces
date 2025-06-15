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

    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    xmn1, xmx1 = x1, x1 + a
    ymn1, ymx1 = y1, y1 + b
    xmn2, xmx2 = x2, x2 + a
    ymn2, ymx2 = y2, y2 + b

    ww = max(xmn2 - xmx1, xmn1 - xmx2)
    hh = max(ymn2 - ymx1, ymn1 - ymx2)

    if ww >= 0 and hh >= 0:
        if ww % a != 0 and hh % b != 0:
            print("NO")
            continue
    elif ww < 0:
        if hh % b != 0:
            print("NO")
            continue
    elif hh < 0:
        if ww % a != 0:
            print("NO")
            continue

    print("YES")
