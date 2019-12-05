# BOJ 15953 - 상금 헌터
import sys
r = sys.stdin.readline
first = [500, 300, 200, 50, 30, 10]
second = [512, 256, 128, 64, 32]

for i in range(int(r())):
    a, b = map(int, r().split())
    money = 0
    if a != 0:
        if a <= 1:
            money += first[0]
        elif a <= 3:
            money += first[1]
        elif a <= 6:
            money += first[2]
        elif a <= 10:
            money += first[3]
        elif a <= 15:
            money += first[4]
        elif a <= 21:
            money += first[5]

    if b != 0:
        if b <= 1:
            money += second[0]
        elif b <= 3:
            money += second[1]
        elif b <= 7:
            money += second[2]
        elif b <= 15:
            money += second[3]
        elif b <= 31:
            money += second[4]

    print(money * 10000)

