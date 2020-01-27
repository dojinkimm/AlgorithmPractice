# 주식 가격 - 스택/큐
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    answer.append(0)
    return answer
