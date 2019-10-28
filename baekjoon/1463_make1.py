# BOJ 1463 - 1로 만들기
import sys

N = int(sys.stdin.readline())
arr = [0] * (N+1)

for i in range(2, N+1):
    arr[i] = arr[i - 1] + 1
    if i % 3 == 0:
        arr[i] = min(arr[i//3] + 1, arr[i])
    elif i % 2 == 0:
        arr[i] = min(arr[i//2] + 1, arr[i])


print(arr[-1])

