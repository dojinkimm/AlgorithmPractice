# 카펫 - 완전탐색
def solution(brown, red):
    total = brown + red
    limit = int(total ** 0.5)

    for i in range(3, limit+1):
        if total % i == 0:
            tmp = total//i
            if (tmp-2) * (i-2) == red:
                return [tmp, i]

solution(10,2)
solution(8,1)
solution(24,24)