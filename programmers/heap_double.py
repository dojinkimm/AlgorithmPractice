# 이중우선순위큐 - Heap
from heapq import heappush, heappop


def solution(operations):
    q = []
    for op in operations:
        alpha, num = map(str, op.split(' '))
        if alpha == 'I':
            heappush(q, int(num))
        elif alpha == 'D' and q:
            if num == '1':
                q = q[:-1]
            else:
                heappop(q)

    if q:
        return [max(q), heappop(q)]
    else:
        return [0, 0]