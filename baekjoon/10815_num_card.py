# BOJ 10815 - 숫자 카드 - 이분 탐색
import sys
r = sys.stdin.readline

def exists(n):
    lo = 0
    hi = N-1
    while lo <= hi:
        mid = (lo+hi)//2
        if sang[mid] == n:
            return True
        elif sang[mid] > num:
            hi = mid-1
        else:
            lo = mid + 1
    return False

N = int(r())
sang = sorted(list(map(int, r().split())))
M = int(r())
for num in list(map(int, r().split())):
    if exists(num):
        print(1, end=" ")
    else:
        print(0, end=" ")