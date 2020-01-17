# BOJ 2563 - 색종이
N = int(input())
paper = [[0]*100 for _ in range(100)]
area = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if paper[i][j] == 0:
                paper[i][j] = 1
                area += 1

print(area)
