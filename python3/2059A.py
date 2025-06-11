for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    la = len(set(a))
    lb = len(set(b))
    if la >= 2 and lb >= 2:
        ans = "YES"
    elif la >= 3 and lb == 1:
        ans = "YES"
    elif lb >= 3 and la == 1:
        ans = "YES"
    else:
        ans = "NO"

    print(ans)