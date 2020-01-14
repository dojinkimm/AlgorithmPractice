# 1620 - 나는야 포켓몬 마스터 이다솜 - 이분 탐색
import sys
r = sys.stdin.readline

def find_pok(poke):
    lo = 0
    hi = N-1
    while lo <= hi:
        mid = (lo+hi)//2
        if pok_sorted[mid][1] == poke:
            return pok_sorted[mid][0]
        elif pok_sorted[mid][1] > poke:
            hi = mid - 1
        else:
            lo = mid + 1


N, M = map(int, r().split())
pokemon = [[i, r().strip()] for i in range(1, N+1)]
pok_sorted = sorted(pokemon, key=lambda x:x[1])
for _ in range(M):
    word = r().strip()
    if word.isdigit():
        print(pokemon[int(word) - 1][1])
    else:
        print(find_pok(word))
