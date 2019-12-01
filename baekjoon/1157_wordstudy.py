# BOJ 1157 - 단어 공부
from collections import Counter
word = input()
if len(word) == 1:
    print(word.upper())
else:
    cnt = Counter(word.lower()).most_common(2)
    if cnt[0][1] == cnt[1][1]:
        print("?")
    else:
        print(cnt[0][0].upper())
