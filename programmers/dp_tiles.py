# 타일 장식물 - DP

def solution(N):
    tile = [0] * N
    tile[0] = 1
    tile[1] = 1
    for i in range(2, N):
        tile[i] = tile[i-1] + tile[i-2]

    return 4*tile[-1] + 2*tile[-2]

solution(5)
solution(6)