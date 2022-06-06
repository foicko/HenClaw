import numpy as np
import sys
# w = [2, 3, 4, 7]
w = []
# v = [1, 3, 5, 9]
v = []
# W = 10
# n = 4
n = int(input())
for k in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
W = int(input())

dp = np.zeros((n + 1, W + 1))
dpi = np.zeros((n + 1, W + 1))
dp = dp.tolist()
dpi = dpi.tolist()
for i in range(n+1):
    for j in range(W+1):
        dp[i][j] = int(dp[i][j])

for i in range(n+1):
    for j in range(W+1):
        dpi[i][j] = int(dpi[i][j])


def _backpack(n, W):
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            nol = dp[i - 1][j]
            if j < w[i - 1]:
                inl = -sys.maxsize
            else:
                inl = dp[i][j - w[i - 1]] + v[i - 1]
            dp[i][j] = max(nol, inl)
            if nol > inl:
                dpi[i][j] = dpi[i - 1][j]
            else:
                dpi[i][j] = i
    return dp, dpi


def output():
    for i in range(n):
        print('F[ ' + (str(i + 1)) + ' ]: ', end="")
        for j in range(W):
            print('{:>5s}'.format(str(dp[i+1][j+1])), end='')
        print("")
    for i in range(n):
        print('i[ ' + (str(i + 1)) + ' ]: ', end="")
        for j in range(W):
            print('{:>5s}'.format(str(dpi[i+1][j+1])), end='')
        print("")


def trace(_n, _W, _w):
    s = dpi
    res = [int(x) for x in np.zeros(_n).tolist()]
    y = _W
    j = _n
    while s[j][y] != 0:
        j = int(s[j-1][y-1])
        res[j - 1] = 1
        y = y - w[j - 1]
        while s[j][y] == j:
            y = y - w[j - 1]
            res[j - 1] = res[j - 1] + 1
    return res


_backpack(n, W)
output()
print(trace(n, W, w))
