# BOJ 9372 - 상근이의 여행
import sys
r = sys.stdin.readline


for _ in range(int(r())):
    N, M = map(int, r().split())
    travel = [list(map(int, r().split())) for _ in range(M)]
    print(N-1)

# 2
# 3 3
# 1 2
# 2 3
# 1 3
# 5 4
# 2 1
# 2 3
# 4 3
# 4 5