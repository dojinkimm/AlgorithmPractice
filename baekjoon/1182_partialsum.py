# 1182 - 부분 수열의 합 - 브루트포스
import sys
r = sys.stdin.readline

def partial_sum(idx, add):
    global cnt
    if idx >= N:
        return

    add += arr[idx]
    if add == S:
        cnt += 1
    # 숫자 더하지 않은 경우
    partial_sum(idx + 1, add - arr[idx])
    # 숫자 더하는 경우
    partial_sum(idx + 1, add)


N, S = map(int, r().split())
arr = list(map(int, r().split()))
cnt = 0

partial_sum(0, 0)
print(cnt)
