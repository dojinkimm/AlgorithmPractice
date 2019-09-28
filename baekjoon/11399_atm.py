# BOJ 11399 - ATM
import sys
from itertools import accumulate

N = int(sys.stdin.readline())

people = sorted(list(map(int, sys.stdin.readline().split())))

print(sum(list(accumulate(people))))
