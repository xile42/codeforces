from math import *
from typing import *
from collections import *
from random import randrange


"""
codeforces-python: 算法竞赛Python3模板库
#1: 基础并查集
https://github.com/xile42/codeforces-python/blob/main/templates/union_find.py
"""
class UnionFind:

    def __init__(self, n: int) -> None:

        self.root = list(range(n))
        self.size = [1] * n  # 并查集大小/秩
        self.count = n  # 连通分量数

    # # 递归写法
    # def find(self, x):
    #
    #     if x != self.root[x]:
    #         self.root[x] = self.find(self.root[x])
    #
    #     return self.root[x]

    # 非递归写法, 效率更优
    def find(self, x: int) -> int:

        root = x
        while self.root[root] != root:
            root = self.root[root]
        while self.root[x] != root:
            self.root[x], x = root, self.root[x]

        return root

    def merge(self, x: int, y: int) -> Optional[int]:

        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return None  # 未发生合并
        # 按秩合并
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.size[root_x] = 0
        self.count -= 1

        return root_y

    def is_merged(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

    def get_parts(self) -> DefaultDict[int, List[int]]:

        parts = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            parts[self.find(i)].append(i)

        return parts

    def get_sizes(self) -> DefaultDict[int, int]:

        sizes = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            sizes[self.find(i)] = self.size[self.find(i)]

        return sizes


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
    ns = list(map(int, input().split()))

    uf = UnionFind(n)
    for i, j in enumerate(ns):
        uf.merge(i, j - 1)

    parts = uf.get_parts()
    ans = [0] * n
    for i in range(n):
        ans[i] = len(parts[uf.find(i)])

    print(" ".join(map(str, ans)))
