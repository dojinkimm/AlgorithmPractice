# BOJ 1932 - 정수 삼각형 - DP
import sys
r = sys.stdin.readline

N = int(r())
tri = [list(map(int,r().split())) for _ in range(N)]
ans = [[-1]*i for i in range(1,N+1)]
ans[0][0] = tri[0][0]

for i in range(1, N):
    for j in range(len(tri[i])):
        if j-1 >= 0 and j+1 < len(tri[i]):
            ans[i][j] = max(ans[i-1][j-1]+tri[i][j], ans[i-1][j]+tri[i][j])
        elif j-1 >= 0:
            ans[i][j] = ans[i-1][j-1]+tri[i][j]
        else:
            ans[i][j] = ans[i-1][j] + tri[i][j]

print(max(ans[N-1]))