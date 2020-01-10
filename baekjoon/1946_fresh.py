# BOJ 1946 - 신입사원 - Greedy
import sys
r = sys.stdin.readline

for _ in range(int(r())):
    N = int(r())
    worker = [0] * (N+1)
    for _ in range(N):
        doc, inter = map(int, r().split())
        worker[doc] = inter

    cnt = 1
    interview = worker[1]
    if interview != 1:
        for i in range(2, N+1):
            if interview > worker[i]:
                cnt += 1
                interview = worker[i]
    print(cnt)

# for _ in range(int(r())):
#     N = int(r())
#     worker = [list(map(int,r().split())) for _ in range(N)]
#     worker.sort(key=lambda x: (x[0], x[1]))
#
#     cnt = 1
#     interview = worker[0][1]
#     for i in range(1, len(worker)):
#         if worker[i][1] < interview:
#             cnt += 1
#             interview = worker[i][1]
#     print(cnt)

