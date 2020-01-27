# 기능개발 - 스택/큐
def solution(progresses, speeds):
    answer = []
    cnt, accumDay = 0, 0
    for prog, sp in zip(progresses, speeds):
        remain = 100 - prog
        if remain % sp == 0:
            day = remain // sp
        else:
            day = remain // sp + 1

        if day > accumDay:
            answer.append(1)
            accumDay = day
        else:
            answer[-1] += 1

    return answer