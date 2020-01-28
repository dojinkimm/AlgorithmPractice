# 디스크 컨트롤러 - Heap
from heapq import heappush, heappop


def solution(jobs):
    time, end, q = 0, -1, []
    answer = 0
    cnt = 0
    length = len(jobs)
    while cnt < length:
        for job in jobs:
            if end < job[0] <= time:
                answer += (time - job[0])
                heappush(q, job[1])

        if len(q) > 0:
            answer += len(q) * q[0]
            end = time
            time += heappop(q)
            cnt += 1
        else:
            time += 1

    return (int(answer / length))