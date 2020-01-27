# 다리를 지나는 트럭 - 스택/큐
from collections import deque


def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    truck = deque(truck_weights)
    time = 0
    while queue:
        time += 1
        queue.popleft()
        if truck:
            if sum(queue) + truck[0] <= weight:
                queue.append(truck.popleft())
            else:
                queue.append(0)

    return time