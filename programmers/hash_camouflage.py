# 위장 - 해시
from collections import Counter


def solution(clothes):
    arr = Counter([x[1] for x in clothes])
    if len(arr) == 1:
        return len(clothes)
    else:
        answer = 1
        for c in arr.items():
            answer *= c[1] + 1
        return answer - 1
