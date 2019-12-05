# 탑 - 스택/큐
def solution(heights):
    length = len(heights)
    answer = [0] * length
    heights.reverse()
    for i, h in enumerate(heights):
        for j in range(i+1,length):
            if heights[j] > h:
                answer[i] = length-j
                break
    return answer[::-1]
