# BOJ 6549 - 히스토그램에서 가장 큰 직사각형 - 분할 정복
import sys
r = sys.stdin.readline


def largest_area(left, right):
    # base case 히스토그램 하나일 때
    if left == right:
        return hist[left]

    mid = (left + right) // 2

    # 분할된 문제 conquer하기
    ret = max(largest_area(left, mid), largest_area(mid+1, right))

    # 2 부분에 걸친 가장 큰 사각형 찾는다
    low = mid
    high = mid+1
    height = min(hist[low], hist[high])

    # [mid, mid+1] 만 포함하는 너비 2의 사각형만 고려한다
    ret = max(ret, height*2)

    # 사각형이 입력을 다 덮을때까지 진행한다
    while left < low or high < right:
        # 높이가 더 큰 히스토그램으로 나아간다
        if high < right and (low == left or hist[low-1] < hist[high+1]):
            high += 1
            height = min(height, hist[high])
        else:
            low -= 1
            height = min(height, hist[low])

        ret = max(ret, height * (high - low + 1))

    return ret


while True:
    get_input = list(map(int, r().split()))

    if get_input[0] == 0:
        break

    N = get_input[0]
    hist = get_input[1:]

    result = largest_area(0, N-1)
    print(result)



