from math import inf


for _ in range(int(input())):

    n = int(input())

    x_mn, x_mx = [inf, inf], [-inf, -inf]
    y_mn, y_mx = [inf, inf], [-inf, -inf]
    xys = list()
    for _ in range(n):
        x, y = map(int, input().split())
        xys.append((x, y))
        x_mn = sorted(x_mn + [x])[:2]
        x_mx = sorted(x_mx + [x], reverse=True)[:2]
        y_mn = sorted(y_mn + [y])[:2]
        y_mx = sorted(y_mx + [y], reverse=True)[:2]

    if n == 1:
        print(1)
        continue

    # print(x_mn, x_mx, y_mn, y_mx)
    xl = (x_mx[0] - x_mn[0] + 1)
    yl = (y_mx[0] - y_mn[0] + 1)
    ans = xl * yl
    # print(xl, yl, xl * yl)

    for x, y in xys:
        if x == x_mn[0]:
            cur_xl = (x_mx[0] - x_mn[1] + 1)
        elif x == x_mx[0]:
            cur_xl = (x_mx[1] - x_mn[0] + 1)
        else:
            cur_xl = xl
        if y == y_mn[0]:
            cur_yl = (y_mx[0] - y_mn[1] + 1)
        elif y == y_mx[0]:
            cur_yl = (y_mx[1] - y_mn[0] + 1)
        else:
            cur_yl = yl

        this_ans = cur_xl * cur_yl
        if this_ans < n:
            this_ans += min(cur_xl, cur_yl)
        ans = min(ans, this_ans)

        # print(cur_xl, cur_yl, cur_xl * cur_yl)

    print(ans)
