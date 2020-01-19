# BOJ 2851 - 슈퍼 마리오
import sys

points = [int(sys.stdin.readline()) for _ in range(10)]
score = 0
for i in range(10):
    if abs(score + points[i] - 100) <= abs(score-100):
        score += points[i]
    else:
        break
print(score)
