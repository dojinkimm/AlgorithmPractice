# BOJ 1074 - Z - 분할 정복
import sys

N, r, c = map(int, sys.stdin.readline().split())
cnt, x, y = 0, 0, 0
n = pow(2, N)

while n:
    n //= 2

    if r < y + n and c < x + n:
        cnt += n * n * 0
    elif r < y + n:
        cnt += n * n * 1
        x += n
    elif c < x + n:
        cnt += n * n * 2
        y += n
    else:
        cnt += n * n * 3
        x += n
        y += n

    if n == 1:
        print(cnt)
        break

# 시간 초과
# dx = [0, 1, 0, 1]
# dy = [0, 0, 1, 1]
#
#
# def iterate_z(n, y, x):
#     global cnt, answer
#     if n == 2:
#         for i in range(4):
#             ndy = y + dy[i]
#             ndx = x + dx[i]
#
#             if ndy == r and ndx == c:
#                 print(cnt)
#                 sys.exit(1)
#             cnt += 1
#
#     else:
#         ns = n // 2
#         iterate_z(ns, y, x)
#         iterate_z(ns, y, x+ns)
#         iterate_z(ns, y+ns, x)
#         iterate_z(ns, y+ns, x+ns)
#
#
# N, r, c = map(int, sys.stdin.readline().split())
# cnt, answer = 0, 0
# iterate_z(2**N, 0, 0)
#
