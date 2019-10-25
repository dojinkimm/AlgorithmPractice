# BOJ 1697 - 숨박꼭질
import sys
from collections import deque

LIMIT = 100001

def solve(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()

        if i == k:
            return arr[i]

        for j in (i+1, i-1, 2*i):
            if (0 <= j < LIMIT) and arr[j] == 0:
                arr[j] = arr[i] + 1
                q.append(j)



        # if (0 <= i+1 < LIMIT) and arr[i+1] == 0:
        #     arr[i+1] = arr[i] + 1
        #     q.append(i+1)
        #
        # if (0 <= i-1 < LIMIT) and arr[i-1] == 0:
        #     arr[i-1] = arr[i] + 1
        #     q.append(i - 1)

        # if (0 <= 2*i < LIMIT) and arr[2*i] == 0:
        #     arr[2*i] = arr[i] + 1
        #     q.append(2 * i)


N, K = map(int, sys.stdin.readline().split())
find = [0] * LIMIT

print(solve(find, N, K))
