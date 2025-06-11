from random import randrange


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
    a = list(map(XorRandomly, map(int, input().split())))
    b = list(map(XorRandomly, map(int, input().split())))

    ans = 0
    ds = [
        dict(),  # up - down - up...
        dict(),  # down - up - down...
    ]
    cur = 0  # ai -> ds[cur], bi -> ds[1 - cur]

    for i in range(n):
        ai, bi = a[i], b[i]
        # 特判
        if ai == bi:
            ans = max(ans, i + 1)
        # 更新当前最大答案
        if ai in ds[1 - cur]:
            ans = max(ans, ds[1 - cur][ai] + 1)
        if bi in ds[cur]:
            ans = max(ans, ds[cur][bi] + 1)
        # 更新删除当前答案
        if i + 1 < n:
            aii, bii = a[i + 1], b[i + 1]
            if aii in ds[1 - cur]:
                ans = max(ans, ds[1 - cur][aii] + 1)
            if bii in ds[cur]:
                ans = max(ans, ds[cur][bii] + 1)
        # ai bi入库
        ds[cur][ai] = i
        ds[1 - cur][bi] = i
        # cur 翻转
        cur = 1 - cur

    # print(ds[0])
    # print(ds[1])

    print(ans)