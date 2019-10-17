# BOJ 9461 - 파도반 수열
import sys

r = sys.stdin.readline

N = int(r())
arr = [int(r()) for _ in range(N)]
seq = [1, 1, 1, 2, 2]

for i in range(5, max(arr)):
    seq.append(seq[i-1]+seq[i-5])

for i in arr:
    print(seq[i-1])
