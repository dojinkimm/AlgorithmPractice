# BOJ 1753 - 프린터 큐
import sys
r = sys.stdin.readline

for i in range(int(r())):
    arr_size, location = map(int, r().split())
    q = list(map(int, r().split()))
    chk = [0 for i in range(arr_size)]
    chk[location] = 'X'
    count = 0

    while True:
        if q[0] == max(q):
            count += 1
            if chk[0] == 'X':
                print(count)
                break
            else:
                q.pop(0)
                chk.pop(0)
        else:
            q.append(q.pop(0))
            chk.append(chk.pop(0))
