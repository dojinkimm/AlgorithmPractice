# 라면 공장 - Heap
from heapq import heappush, heappop


def solution(stock, dates, supplies, k):
    answer = 0
    j = 0
    q = []
    while stock < k:
        for i in range(j, len(dates)):
            if stock < dates[i]:
                break
            heappush(q, -supplies[i])
            j = i + 1

        stock += (heappop(q) * -1)
        answer += 1

    return answer