# BOJ 2490 - 윷놀이
import sys

yut = ["D", "C", "B", "A", "E"]

for _ in range(3):
    turn = list(map(int, sys.stdin.readline().split()))
    print(yut[turn.count(1)])
