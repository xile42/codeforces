for _ in range(int(input())):

    n = int(input())
    ns = list(map(int, input().split()))

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    ans = [0 for _ in range(n + 1)]
    ans[1] = ns[0]

    # def dfs(node, par, score_par, score_gpar):
    #
    #     # print("f({}, {}, {}, {})".format(node, par, score_par, score_gpar))
    #     if node != 1:
    #         ans[node] = max(ns[node - 1], ns[node - 1] + score_gpar - ns[par - 1])
    #     # print(ans[node])
    #     for next_node in g[node]:
    #         if next_node == par:
    #             continue
    #         dfs(next_node, node, ans[node], score_par)


    def dfs_stack(g, ns, ans):

        stack = [(1, -1, 0, 0)]  # (node, par, score_par, score_gpar)

        while stack:

            node, par, score_par, score_gpar = stack.pop()
            if node != 1:
                ans[node] = max(ns[node - 1], ns[node - 1] + score_gpar - ns[par - 1])

            for next_node in g[node]:
                if next_node == par:
                    continue
                stack.append((next_node, node, ans[node], score_par))

        return ans

    ans = dfs_stack(g, ns, ans)

    print(" ".join(map(str, ans[1:])))
