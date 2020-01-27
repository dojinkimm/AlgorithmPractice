# 쇠막대기 - 스택/큐
def solution(arrangement):
    answer = 0
    stack = []

    for idx, a in enumerate(arrangement):
        if a == '(':
            stack.append(a)
        else:
            stack.pop()
            if arrangement[idx - 1] == '(':
                answer += len(stack)
            else:
                answer += 1
    return answer