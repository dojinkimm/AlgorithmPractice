# 등굣길 - DP

def solution(m, n, puddles):
    MOD = 1000000007
    way = [[0] * m for _ in range(n)]
    way[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i is 0 and j is 0:
                continue
            elif [j+1, i+1] in puddles:
                way[i][j] = 0
            else:
                way[i][j] = (way[i-1][j] + way[i][j-1]) % MOD

    return way[n-1][m-1] % MOD


solution(4, 3, [[2,2]])
