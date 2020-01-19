import sys
r = sys.stdin.readline
N = int(r())
M = int(r())
friends = dict()
visited = set()
for _ in range(M):
    a, b = map(int, r().split())
    if a not in friends:
        friends[a] = [b]
    else:
        friends[a].append(b)

    if b not in friends:
        friends[b] = [a]
    else:
        friends[b].append(a)

for frs in friends[1]:
    visited.add(frs)
    for f in friends[frs]:
        visited.add(f)
print(len(visited)-1)