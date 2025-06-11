d = {"p": "q", "q": "p", "w": "w"}

for _ in range(int(input())):
    w = input()[::-1]
    print("".join([d[c] for c in w]))
