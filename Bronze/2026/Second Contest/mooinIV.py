first = input().strip().split()
t, k = int(first[0]), int(first[1])

for i in range(t):
    parityOn = 0
    n = int(input().strip())
    s = input().strip()
    keystrokes = []
    for i in range(n-1, -1, -1):
        if parityOn == 0:
            if s[i] == "M":
                keystrokes.append("M")
            elif s[i] == "O":
                parityOn = (parityOn + 1) % 2
                keystrokes.append("O")
        elif parityOn == 1:
            if s[i] == "O":
                keystrokes.append("M")
            elif s[i] == "M":
                parityOn = (parityOn + 1) % 2
                keystrokes.append("O")
    print("YES")
    if k == 1:
        print("".join(keystrokes[::-1]))