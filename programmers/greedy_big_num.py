# 큰 수 만들기 - 그리디
def solution(number, k):
    compare = [number[0]]
    for i in range(1, len(number)):
        while compare and compare[-1] < number[i] and k > 0:
            compare.pop()
            k -= 1
        if k == 0:
            compare.extend(number[i:])
            break
        compare.append(number[i])

    compare = compare[:-k] if k > 0 else compare
    return "".join(compare)