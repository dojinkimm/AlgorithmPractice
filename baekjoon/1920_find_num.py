# BOJ 1920 - 수 찾기 - 이분 탐색
import sys
r = sys.stdin.readline

N = int(r())
A = sorted(list(map(int, r().split())))
M = int(r())
for num in list(map(int, r().split())):
    lo = 0
    hi = len(A)-1
    flag = False
    while lo <= hi:
        mid = (lo+hi)//2
        if A[mid] == num:
            print(1)
            flag = True
            break
        elif A[mid] < num:
            lo = mid+1
        else:
            hi = mid-1

    if not flag:
        print(0)
