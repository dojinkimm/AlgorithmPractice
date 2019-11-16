# BOJ 10989 - 수 정렬하기 3
import sys
r = sys.stdin.readline

arr = [0] * 10001
for i in range(int(r())):
    arr[int(r())] += 1
for i in range(10001):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i)
