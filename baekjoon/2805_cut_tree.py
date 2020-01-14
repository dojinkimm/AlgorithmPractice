# BOJ 2805 - 나무 자르기 - 이분 탐색
import sys
r = sys.stdin.readline


def is_possible(height):
    cnt = 0
    for tr in trees:
        if tr - height > 0:
            cnt += (tr - height)
    return cnt


N, M = map(int, r().split())
trees = list(map(int, r().split()))
lo, hi = 0, max(trees)
mid = 0
answer = 0
flag = False
while lo <= hi:
    mid = (lo+hi)//2
    count = is_possible(mid)
    if count == M:
        flag = True
        break
    elif count > M:
        lo = mid + 1
        answer = max(answer, mid)
    else:
        hi = mid - 1
if flag:
    print(mid)
else:
    print(answer)