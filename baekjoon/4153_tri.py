# BOJ 4153 - 직각삼각형

while True:
    tri = list(map(int, input().split()))
    if tri.count(0) == 3:
        break
    for i in range(3):
        tri[i] = pow(tri[i], 2)
    c = max(tri)
    if sum(tri) == c*2:
        print("right")
    else:
        print("wrong")