# BOJ 1120 - 문자열 - Greedy
import sys

A, B = sys.stdin.readline().strip().split()
cnt = []
for i in range(len(B)-len(A)+1):
    maximum = 0
    for a, b in zip(A, B[i:]):
        if a != b:
            maximum += 1
    cnt.append(maximum)
print(min(cnt))
