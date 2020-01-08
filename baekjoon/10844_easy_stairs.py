# BOJ 10844 - 쉬운 계단 수 - DP
import sys

DIV = 1000000000

N = int(sys.stdin.readline())
stair = [[1]*10 for _ in range(N+1)]

stair[0][0] = 0
for i in range(1, N+1):
    for j in range(10):
        if j == 0:
            stair[i][0] = stair[i-1][1]
        elif j == 9:
            stair[i][9] = stair[i-1][8]
        else:
            stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]

print(sum(stair[N-1]) % DIV)