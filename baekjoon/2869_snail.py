# BOJ 2869 - 달팽이는 올라가고 싶다 - 이분탐색
import sys

A, B, V = map(int, sys.stdin.readline().split())
if V == A:
    print(1)
else:
    days = (V - B - 1) // (A-B) + 1
    print(days)