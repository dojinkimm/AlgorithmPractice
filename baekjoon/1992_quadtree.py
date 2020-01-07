# # BOJ 1992 - 쿼드 트리 - 분할 정복
import sys
r = sys.stdin.readline


def decompose(n, y, x):
    # print(n, y, x)
    if n == 1:
        print(image[y][x], end="")
        return

    flag = True
    for i in range(y, y+n):
        if not flag:
            break
        for j in range(x, x+n):
            if image[i][j] != image[y][x]:
                flag = False
                break

    if flag:
        print(image[y][x], end="")
    else:
        decreased_n = n//2

        print("(", end="")
        decompose(decreased_n, y, x)
        decompose(decreased_n, y, x+decreased_n)
        decompose(decreased_n, y+decreased_n, x)
        decompose(decreased_n, y+decreased_n, x+decreased_n)
        print(")", end="")


N = int(r())
image = [list(r().strip()) for _ in range(N)]
decompose(N, 0, 0)
