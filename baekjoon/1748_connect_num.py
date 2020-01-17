# BOJ 1748 - 수 이어 쓰기 1
N = int(input())
answer = 0
length = len(str(N))
while N > 0:
    num = N - pow(10, length-1)
    answer += ((num+1) * length)
    N -= (num+1)
    length -= 1
print(answer)
