# BOJ 11728 - 하노이 탑 이동 순서 - 분할 정복
import sys


def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        movement.append([from_rod, to_rod])
        return
    hanoi(n - 1, from_rod, aux_rod, to_rod)
    movement.append([from_rod, to_rod])
    hanoi(n - 1, aux_rod, to_rod, from_rod)


N = int(sys.stdin.readline())
movement = []
hanoi(N, 1, 3, 2)
print(len(movement))
for m in movement:
    print(m[0], m[1])

