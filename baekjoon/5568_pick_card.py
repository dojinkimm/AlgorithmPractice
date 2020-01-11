# BOJ 5568 - 카드 놓기 - 조합론
import sys
r = sys.stdin.readline

def solution(picked):
    if picked == k:
        s = ""
        for i in range(len(selected)):
            change = str(selected[i])
            s = s + change
        answer.add(s)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            selected.append(cards[i])
            solution(picked + 1)
            visited[i] = False
            selected.pop()


n = int(r())
k = int(r())
cards = sorted([int(r()) for _ in range(n)])
visited = [False] * n
selected = list()
answer = set()

solution(0)
print(len(answer))
