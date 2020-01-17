# 징검다리 - 이분 탐색

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    answer = 0
    lo, hi = 1, distance
    while lo <= hi:
        cnt, prev = 0, 0
        mid = (lo + hi) // 2

        for i in range(len(rocks)):
            if rocks[i] - prev <= mid:
                cnt += 1
            else:
                prev = rocks[i]

        if cnt <= n:
            lo = mid + 1
        else:
            answer = mid
            hi = mid - 1

    return answer