# BOJ 9251 - LCS
import sys
r = sys.stdin.readline

w1 = r().strip() # 행
w2 = r().strip() # 열
lcs = [[0] * (len(w2)+1) for _ in range(len(w1)+1)]

for i in range(1, len(w1)+1):
    for j in range(1, len(w2)+1):
        if w1[i-1] == w2[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])
# ACAYKP
# CAPCAKC