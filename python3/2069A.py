for _ in range(int(input())):

    n = int(input())
    ns = list(map(int, input().split(" ")))
    success = True
    for i in range(n - 2):
        if ns[i:i + 3] == [1, 0, 1]:
            success = False
            break

    print("YES" if success else "NO")