# BOJ 14888 - 연산자 끼워놓기 - 브루트 포스
import sys

r = sys.stdin.readline


def find_min_max(idx, result, copy_op_num):
    global minimum, maximum
    if idx == N - 1:
        minimum = min(minimum, result)
        maximum = max(maximum, result)
        return
    for i in range(4):
        if copy_op_num[i] is not 0:
            copy_op_num[i] -= 1
            if operator[i] is "+":
                find_min_max(idx + 1, result + arr[idx + 1], list(copy_op_num))
            elif operator[i] is "-":
                find_min_max(idx + 1, result - arr[idx + 1], list(copy_op_num))
            elif operator[i] is "*":
                find_min_max(idx + 1, result * arr[idx + 1], list(copy_op_num))
            else:
                if result < 0:
                    result = -(abs(result) // arr[idx+1])
                else:
                    result = result // arr[idx+1]
                find_min_max(idx + 1, result, list(copy_op_num))
            copy_op_num[i] += 1

operator = ["+", "-", "*", "//"]
N = int(r())
arr = list(map(int, r().split()))
op_num = list(map(int, r().split()))
minimum = 1000000000
maximum = -1000000000

find_min_max(0, arr[0], list(op_num))
print(maximum)
print(minimum)
