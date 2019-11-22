# 모의고사 - 완전탐색
def solution(answers):
    answer = [0, 0, 0]
    problem = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for idx, num in enumerate(answers):
        if problem[0][idx % 5] == num:
            answer[0] += 1

        if problem[1][idx % 8] == num:
            answer[1] += 1

        if problem[2][idx % 10] == num:
            answer[2] += 1

    arr = [i + 1 for i, n in enumerate(answer) if n == max(answer)]
    return arr
