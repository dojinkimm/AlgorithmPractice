# BOJ 2580 - 스도쿠
import sys
r = sys.stdin.readline


def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True


def vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True


def bythree(x, y, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+j]:
                return False
    return True


def DFS(index):
    if index == len(zeros):
        for row in sudoku:
            for n in row:
                print(n, end=" ")
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            nx = zeros[index][0]
            ny = zeros[index][1]

            if horizontal(nx, i) and vertical(ny, i) and bythree(nx, ny, i):
                sudoku[nx][ny] = i
                DFS(index+1)
                sudoku[nx][ny] = 0


sudoku = [list(map(int, r().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
DFS(0)

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0