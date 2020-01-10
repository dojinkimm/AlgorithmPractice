# BOJ 10610 - 30 - Greedy
import sys

N = sys.stdin.readline().strip()

if '0' not in N:
    print(-1)
else:
    nums = list(reversed(sorted(N)))
    digits = sum(list(map(int, nums)))
    if digits % 3 == 0:
        print("".join(nums))
    else:
        print(-1)
    