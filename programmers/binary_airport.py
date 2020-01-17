# 입국 심사 - 이분 탐색

def take_time(ts, time):
    people = 0
    for t in ts:
        people += (time // t)
    return people


def solution(n, times):
    times.sort()
    lo = 1
    hi = times[-1] * n
    answer = hi
    mid = 0
    while lo <= hi:
        mid = (lo + hi) // 2

        people = take_time(times, mid)
        if people < n:
            lo = mid + 1
        else:
            answer = min(answer, mid)
            hi = mid - 1

    return answer