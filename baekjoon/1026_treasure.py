# BOJ 1026 - 보물
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

answer = sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))])
print(answer)