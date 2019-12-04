# BOJ 9935 - 문자열 폭발
import sys
r = sys.stdin.readline

word = r().strip()
expl = r().strip()
ret = ""
expl_len = len(expl)

for w in word:
    ret += w
    if expl in ret:
        ret = ret[:-expl_len]

print(ret if ret != "" else "FRULA")


# mirkovC4nizCC44
# C4

# 12ab112ab2ab
# 12ab