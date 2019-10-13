# BOJ 9663 - N-Queen
import sys


def place_queen(queen_pos):
    answer = 0
    n = len(queen_pos)
    if n == N:
        return 1
    for i in range(N):
        for j in range(n):
            if i == queen_pos[j]:
                break
            if n - j == i - queen_pos[j]:
                break
            if n - j == queen_pos[j] - i:
                break
        else:
            answer += place_queen(queen_pos + [i])
    return answer


N = int(sys.stdin.readline())
print(place_queen([]))

