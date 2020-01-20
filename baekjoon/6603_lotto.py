# BOJ 6603 - 로또
import sys
from itertools import combinations

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    for p in combinations(arr[1:], 6):
        print(" ".join(map(str, p)))
    print()
