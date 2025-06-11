for _ in range(int(input())):
    n = int(input())
    cnt = input().count("1")
    ans1 = 1 if cnt & 1 else 0
    ans2 = cnt if cnt <= n else n * 2 - cnt
    print("{} {}".format(ans1, ans2))
