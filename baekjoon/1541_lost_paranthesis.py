# BOJ 1541 - 잃어버린 괄호
import sys
import re

# +,- 기준으로 split하고 delimiter도 없애지 않는다
equation = re.split("(\\+|-)", sys.stdin.readline().strip())

plus_repeat = index = 0
for i in range(1, len(equation), 2):
    # 더하기면 두 숫자를 더하고 뒷숫자를 0으로 변환
    if equation[i] == "+":
        if plus_repeat == 0 and index == 0:
            equation[i - 1] = (int(equation[i-1])+int(equation[i+1]))
            equation[i + 1] = 0
            index = i - 1
            plus_repeat += 1
        else:
            # 만약 +가 반복되면 첫 숫자에 누적 더해준ㄴ다
            equation[index] += int(equation[i + 1])
            equation[i + 1] = 0
    else:
        plus_repeat = index = 0

answer = int(equation[0])
for i in range(2, len(equation), 2):
    answer -= int(equation[i])

print(answer)


""" Best Solution
n = [sum(int(x) for x in y.split('+')) for y in input().split('-')]
print(n[0] - sum(n[1:]))
"""
