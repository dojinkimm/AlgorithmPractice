# BOJ 2985 - 세 수
import sys

A, B, C = map(int, sys.stdin.readline().split())
if A + B == C:
    print("{}{}{}={}".format(A, "+", B, C))
elif A - B == C:
    print("{}{}{}={}".format(A, "-", B, C))
elif A * B == C:
    print("{}{}{}={}".format(A, "*", B, C))
elif A == B * C:
    print("{}{}{}={}".format(A, "/", B, C))
elif A == B - C:
    print("{}={}{}{}".format(A, B, "-", C))
else:
    print("{}={}{}{}".format(A, B, "/", C))
