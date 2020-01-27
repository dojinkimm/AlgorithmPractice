# 타겟 넘버 - DFS/BFS
def solution(numbers, target):
    cnt = 0

    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal cnt
                cnt += 1
            return
        dfs(idx + 1, result + numbers[idx])
        dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return cnt