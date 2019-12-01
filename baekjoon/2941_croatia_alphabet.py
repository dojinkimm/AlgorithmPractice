# BOJ 2941 - 크로아티아 알파벳

word = input()

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    if i in word:
        word = word.replace(i, "*")
print(len(word))
