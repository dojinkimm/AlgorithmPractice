# 프린터 - 스택/큐
def solution(priorities, location):
    order = [0] * len(priorities)
    cnt, divide = 1, 0
    for i in range(len(priorities)):
        maximum = max(priorities)
        if divide != 0 and maximum == max(priorities[divide:]):
            idx = priorities[divide:].index(maximum) + divide
        else:
            idx = priorities.index(maximum)
        order[idx] = cnt
        cnt += 1
        divide = idx
        priorities[idx] = 0

    return order[location]