# BOJ 1003 - 피보나치
import sys
r = sys.stdin.readline
c0=[1, 0, 1]
c1=[0, 1, 1]


def fibo(n):
    l = len(c0)
    if l <= n:
        for i in range(l, n+1):
            c0.append(c0[i-1]+c0[i-2])
            c1.append(c1[i-1]+c1[i-2])
    print(c0[n], c1[n])


N = int(r())
for _ in range(N):
    fibo(int(r()))
