# BOJ 11051 - 이항계수 2
import sys

N, K = map(int, sys.stdin.readline().split())
a = 1
for i in range(K):
    a = a * (N-i) // (i+1)
print(a % 10007)
