# BOJ 2875 - 대회 or 인턴 - Greedy
import sys

N, M, K = map(int, sys.stdin.readline().split())
answer = min((N+M-K)//3, N//2, M)
print(answer)
# for _ in range(K):
#     if N >= 2*M:
#         N -= 1
#     else:
#         M -= 1
# if N >= 2*M:
#     print(M)
# else:
#     print(N//2)