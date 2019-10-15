# BOJ 2580 - 스도쿠 v2
import sys
import copy
r = sys.stdin.readline


def backtracking(li, index, m, b, h, v):
    if index >= len(li):
        return True
    y, x = li[index]
    yy = y // 3
    xx = x // 3
    for k in range(1, 10):
        if b[yy][xx][k] or h[x][k] or v[y][k]: continue
        m[y][x] = k
        b[yy][xx][k] = 1
        h[x][k] = 1
        v[y][k] = 1
        if backtracking(li, index + 1, m, b, h, v):
            return True
        else:
            m[y][x] = 0
            b[yy][xx][k] = 0
            h[x][k] = 0
            v[y][k] = 0
    return False


sudoku = [list(map(int, r().split())) for _ in range(9)]
zeros = []
b = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]
h = [[0 for _ in range(10)] for _ in range(10)]
v = copy.deepcopy(h)

for y in range(9):
    for x in range(9):
        t = sudoku[y][x]
        if t == 0:
            zeros.append((y, x))
        yy = y // 3
        xx = x // 3
        b[yy][xx][t] = 1
        h[x][t] = v[y][t] = 1

backtracking(zeros, 0, sudoku, b, h, v)

for y in range(9):
    for x in range(9):
        print(sudoku[y][x], end = " ")
    print()
