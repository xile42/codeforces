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


for _ in range(int(input())):

    m, n = map(int, input().split())
    grid = list()
    for _ in range(m):
        grid.append(list(map(int, input().split())))

    ans = 0
    vis = [[False] * n for _ in range(m)]

    def f(i, j):

        ans = 0
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            if vis[i][j]:
                continue
            vis[i][j] = True
            ans += grid[i][j]
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < m and 0 <= jj < n and not vis[ii][jj] and grid[ii][jj]:
                    queue.append((ii, jj))

        return ans

    for i in range(m):
        for j in range(n):
            if grid[i][j] and not vis[i][j]:
                ans = max(ans, f(i, j))

    print(ans)
