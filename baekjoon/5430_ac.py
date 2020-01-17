# BOJ 5430 - AC
import sys
r = sys.stdin.readline

N = int(r())
for _ in range(N):
    func = r().strip()
    n = int(r())
    if n == 0:
        arr = r().strip()
        arr = []
    else:
        arr = list(map(int, r().strip()[1:-1].split(',')))
    is_reversed = False
    front = 0
    rear = 0

    for f in func:
        if f == 'R':
            is_reversed = not is_reversed
        elif f == 'D' and is_reversed:
            rear += 1
        elif f == 'D' and not is_reversed:
            front += 1

    if front + rear <= n:
        if not is_reversed:
            arr = arr[front: n - rear]
            print(str(arr).replace(' ', ''))
        else:
            arr = arr[::-1][rear:n - front]
            print(str(arr).replace(' ', ''))
    else:
        print('error')
