for _ in range(int(input())):
    n = int(input())
    ns = "|" + "||".join(input().split(" ")) + "|"
    res = [i for i in ns.split("|0|") if len(i) > 0]
    if len(res) == 0:
        print("0")
    elif len(res) == 1:
        print("1")
    else:
        print("2")
