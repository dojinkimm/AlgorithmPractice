# 여행 경로 - DFS/BFS
def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]), reverse=True)
    airport = dict()
    for t in tickets:
        airport[t[0]] = airport.get(t[0], []) + [t[1]]

    answer = ['ICN']
    path = []
    while answer:
        top = answer[-1]

        if top not in airport or len(airport[top]) == 0:
            path.append(answer.pop())
        else:
            answer.append(airport[top][-1])
            airport[top].pop()

    return path[::-1]