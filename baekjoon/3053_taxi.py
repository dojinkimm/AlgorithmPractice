# BOJ 3053 - 택시 기하학
from math import pi

R = int(input())
euclid = R*R*pi
taxi = R*R*2
print(round(euclid, 4))
print(round(taxi, 4))
