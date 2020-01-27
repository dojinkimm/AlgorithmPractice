# 단어 변환 - DFS/BFS
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append(begin)
    visited = [False] * len(words)

    answer = []
    cnt = 0
    while q:
        cnt += 1
        for i in range(len(q)):
            find = q.popleft()

            if find == target:
                answer.append(cnt)

            for idx, w in enumerate(words):
                diff = 0
                if w is not find and not visited[idx]:
                    for i, j in zip(w, find):
                        if i is not j:
                            diff += 1
                    if diff == 1:
                        visited[idx] = True
                        q.append(w)

    return min(answer) - 1