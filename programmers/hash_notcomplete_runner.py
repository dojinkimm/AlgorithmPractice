# 완주하지 못한 선수 - 해시
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.elements())[0]
