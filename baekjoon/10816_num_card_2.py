# BOJ 10816 - 숫자 카드2 - 이분 탐색
import sys
from collections import Counter
r = sys.stdin.readline

N = int(r())
sang = sorted(list(map(int, r().split())))
cnt = Counter(sang)
M = int(r())
for num in list(map(int, r().split())):
    print(cnt[num], end=" ")
