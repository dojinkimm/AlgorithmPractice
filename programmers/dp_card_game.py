# 카드 게임 - DP


def solution(left, right):
    dp = [[0 for x in range(len(left) + 1)] for y in range(len(right) + 1)]
    for i in range(1, len(left) + 1):
        for j in range(1, len(right) + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
            if right[j - 1] < left[i - 1]:
                dp[i][j] = dp[i][j - 1] + right[j - 1]
    return dp[len(left)][len(right)]


solution([3,2,5],[2,4,1])