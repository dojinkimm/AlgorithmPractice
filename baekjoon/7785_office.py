# BOJ 7785 - 회사에 있는 사람
import sys
r = sys.stdin.readline

N = int(r())
people = dict()
for _ in range(N):
    name, status = map(str, r().strip().split())
    if status == 'enter':
        people[name] = True
    else:
        del people[name]

for name in sorted(people.keys(), reverse=True):
    print(name)
