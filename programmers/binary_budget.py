# 예산 - 이분 탐색

def in_limit(cut, bud):
    add = 0
    for b in bud:
        add += min(cut, b)

    return add


def solution(budgets, M):
    answer = 0
    if sum(budgets) <= M:
        return max(budgets)
    lo = 0
    hi = max(budgets)

    while lo <= hi:
        mid = (lo + hi) // 2

        summed = in_limit(mid, budgets)
        if summed <= M:
            lo = mid + 1
            answer = mid
        else:
            hi = mid - 1

    return answer