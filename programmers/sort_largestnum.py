# 가장큰ㄴ수 - 정렬
def solution(numbers):
    numbers = sorted(list(map(str,numbers)), key=lambda x:x*3)
    return str(int("".join(numbers[::-1])))
