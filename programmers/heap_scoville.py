# 더 맵게 - Heap
from heapq import heappush, heappop


def solution(scoville, K):
    answer = 0
    q = []
    for scov in scoville:
        heappush(q, scov)

    flag = False
    while len(q) > 1:
        least = heappop(q)
        least_second = heappop(q)
        new_food = least + (least_second * 2)
        heappush(q, new_food)
        answer += 1

        if all(scov >= K for scov in q):
            flag = True
            break
    return answer if flag else -1