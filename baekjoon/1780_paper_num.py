# BOJ 1780 - 종이의 개수
import sys
r = sys.stdin.readline


def cnt_paper(n, y, x):
    if n == 1:
        cnt[paper[y][x] + 1] += 1
        return

    flag = True
    for i in range(y, y + n):
        for j in range(x, x + n):
            if paper[y][x] != paper[i][j]:
                flag = False
                break
        if not flag:
            break

    if flag and n is not 1:
        cnt[paper[y][x] + 1] += 1
    else:
        n //= 3

        for i in range(3):
            for j in range(3):
                cnt_paper(n, y + (i*n), x + (j*n))


N = int(r())
paper = [list(map(int, r().split())) for _ in range(N)]
cnt = [0] * 3
cnt_paper(N, 0, 0)
for c in cnt:
    print(c)