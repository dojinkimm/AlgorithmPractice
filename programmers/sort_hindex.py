# H-index - 정렬
def solution(citations):
    answer = 0
    citations.sort()
    for ans in range(1,len(citations)+1)[::-1]:
        if citations[-ans] >= ans:
            return ans
    return answer
