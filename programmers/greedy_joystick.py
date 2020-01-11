# 조이스틱 - 그리디
def solution(name):
    A, Z = 65, 90
    answer = 0
    turn = len(name) - 1
    for idx, letter in enumerate(name):
        if Z - ord(letter) > ord(letter) - A:
            answer += ord(letter) - A
        else:
            answer += Z - ord(letter) + 1

        next = idx + 1
        while next < len(name) and name[next] is 'A':
            next += 1

        turn = min(turn, idx + len(name) - next + min(idx, len(name) - next))

    return answer + turn


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])

