# BOJ 4948 - 베르트랑 공준
import sys
r = sys.stdin.readline

numbers = []
while True:
    numbers.append(int(r()))
    if numbers[-1] is 0:
        numbers.pop()
        break

MAX = max(numbers) * 2
isPrime = [False, False] + [True] * (MAX-1)
primes = []
for i in range(2, MAX+1):
    if isPrime[i]:
        primes.append(i)
        for j in range(i*2, MAX+1, i):
            isPrime[j] = False

for i in numbers:
    cnt = isPrime[i+1 : 2*i+1].count(True)
    print(cnt)