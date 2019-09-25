# BOJ 1931 - 회의실배정
import sys

N = int(sys.stdin.readline())
meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)], key=lambda x: (x[1], x[0]))

end = answer = 0
for m in meeting:
    if end <= m[0]:
        end = m[1]
        answer += 1
print(answer)
