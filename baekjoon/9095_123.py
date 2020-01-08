# BOJ 9095 - 1,2,3 더하기 - DP
import sys
r = sys.stdin.readline

arr = [0] * 11
arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 11):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
for _ in range(int(r())):
    num = int(r())
    print(arr[num])


