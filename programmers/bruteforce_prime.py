# 소수찾기 - 완전탐색
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 is 0 or n % 3 is 0:
        return False
    if n < 9:
        return True
    k, l = 5, n ** 0.5
    while k <= l:
        if n % k is 0 or n % (k+2) is 0:
            return False
        k += 6
    return True


def solution(numbers):
    num_string = list(numbers)
    answer = []
    for i in range(1, len(num_string)+1):
        for p in permutations(num_string, i):
            num = int("".join(p))
            if num not in answer and is_prime(num):
                answer.append(num)

    return answer


solution("17")
solution("011")