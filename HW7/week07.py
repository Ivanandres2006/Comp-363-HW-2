a_space = 1

def a(x, y):
    if x == y:
        return 0
    return 5

def build(X, Y):
    m = len(X)
    n = len(Y)
    P = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        P[i][0] = i
    for j in range(n+1):
        P[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            P[i][j] = min(
                P[i-1][j-1] + a(X[i-1], Y[j-1]),
                P[i-1][j] + a_space,
                P[i][j-1] + a_space
            )
    return P

def align(X, Y, P):
    i = len(X)
    j = len(Y)
    ax = ""
    ay = ""

    while i > 0 or j > 0:
        if i > 0 and j > 0 and P[i][j] == P[i-1][j-1] + a(X[i-1], Y[j-1]):
            ax = X[i-1] + ax
            ay = Y[j-1] + ay
            i -= 1
            j -= 1
        elif i > 0 and P[i][j] == P[i-1][j] + a_space:
            ax = X[i-1] + ax
            ay = "-" + ay
            i -= 1
        else:
            ax = "-" + ax
            ay = Y[j-1] + ay
            j -= 1

    return ax, ay

a_space = 1

def a(x, y):
    if x == y:
        return 0
    return 5

def build(X, Y):
    m = len(X)
    n = len(Y)
    P = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        P[i][0] = i
    for j in range(n+1):
        P[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            P[i][j] = min(
                P[i-1][j-1] + a(X[i-1], Y[j-1]),
                P[i-1][j] + a_space,
                P[i][j-1] + a_space
            )
    return P

def align(X, Y, P):
    i = len(X)
    j = len(Y)
    ax = ""
    ay = ""

    while i > 0 or j > 0:
        if i > 0 and j > 0 and P[i][j] == P[i-1][j-1] + a(X[i-1], Y[j-1]):
            ax = X[i-1] + ax
            ay = Y[j-1] + ay
            i -= 1
            j -= 1
        elif i > 0 and P[i][j] == P[i-1][j] + a_space:
            ax = X[i-1] + ax
            ay = "-" + ay
            i -= 1
        else:
            ax = "-" + ax
            ay = Y[j-1] + ay
            j -= 1

    return ax, ay

def stats(ax, ay):
    match = 0
    mismatch = 0
    gap = 0

    for i in range(len(ax)):
        if ax[i] == "-" or ay[i] == "-":
            gap += 1
        elif ax[i] == ay[i]:
            match += 1
        else:
            mismatch += 1

    return match, mismatch, gap

def run(X, Y):
    P = build(X, Y)
    ax, ay = align(X, Y, P)
    m, mm, g = stats(ax, ay)

    print(X, "--> |" + ax + "|    matches:", m, ", mismatches:", mm)
    print(Y, "--> |" + ay + "|    gaps:", g)
    print()

tests = [
    ["CRANE", "RAIN"],
    ["CYCLE", "BICYCLE"],
    ["ASTRONOMY", "GASTRONOMY"],
    ["INTENTION", "EXECUTION"],
    ["AGGTAB", "GXTXAYB"],
    ["GATTACA", "GCATGCU"],
    ["DELICIOUS", "RELIGIOUS"],
]

for t in tests:
    run(t[0], t[1])