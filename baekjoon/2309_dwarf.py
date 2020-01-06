# BOJ 2309 - 일곱 난쟁이
import sys
r = sys.stdin.readline
TRUE_DWARF = 7
check = [False for _ in range(9)]


def find_true_dwarfs(index, cnt, total_num):
    if cnt == TRUE_DWARF:
        if total_num == 100:
            for i, dwarf in enumerate(heights):
                if check[i]:
                    array.append(dwarf)
            return True
    else:
        for i in range(index, 9):
            check[i] = True
            if find_true_dwarfs(i+1, cnt+1, total_num + heights[i]):
                return True
            check[i] = False
            if find_true_dwarfs(i+1, cnt, total_num):
                return True
    return False


heights = [int(r()) for _ in range(9)]
array = []
find_true_dwarfs(0, 0, 0)
for a in sorted(array):
    print(a)