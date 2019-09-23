# BOJ 2798 - 블랙잭
import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(0,len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1,len(card)):
            num = card[i] + card[j] + card[k]
            if answer < num < M:
                answer = num
            elif num == M:
                answer = num
                break
print(answer)
