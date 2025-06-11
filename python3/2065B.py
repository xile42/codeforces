for _ in range(int(input())):
    s = input()
    found = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            found = True
            break
    print(1 if found else len(s))