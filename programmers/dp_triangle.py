# 정수 삼각형 - DP

def solution(triangle):
    length = len(triangle)
    tri = [[0]*(i+1) for i in range(len(triangle))]
    tri[0] = triangle[0][:]
    for i in range(1, length):
        for j in range(i+1):
            if j == 0:
                tri[i][j] = tri[i-1][j] + triangle[i][j]
            elif j == i:
                tri[i][j] = tri[i-1][i-1] + triangle[i][j]
            else:
                tri[i][j] = max(tri[i-1][j], tri[i-1][j-1]) + triangle[i][j]
    return max(tri[-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
