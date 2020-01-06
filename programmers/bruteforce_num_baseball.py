# 숫자 야구 - 완전탐색
def solution(baseball):
    answer, strike, ball = 0, 0, 0
    for i in range(123, 988):
        num1 = str(i)
        if '0' in num1:
            continue
        if num1[0] is num1[1] or num1[0] is num1[2] or num1[1] is num1[2]:
            continue

        flag = True
        for b in baseball:
            strike, ball = 0, 0
            for a in range(3):
                for k in range(3):
                    num2 = str(b[0])
                    if a == k and num1[a] == num2[k]:
                        strike += 1
                        continue
                    if a != k and num1[a] == num2[k]:
                        ball += 1
                        continue

            if strike != b[1] or ball != b[2]:
                flag = False
                break

        if flag:
            answer += 1
    return answer


    # for b in baseball:
    #     num = str(b[0])
    #
    #     # strike라면
    #     if b[1] > 0:
    #         # 3자리 수 다 맞춤
    #         if b[1] == 3:
    #             return 1
    #         elif b[1] == 2:
    #             possible = [p for p in possible if num[:2] in p[:2]
    #                         or num[1if '0' not in str(i)
    #                 and str(i)[0] not in str(i)[1:]
    #                 and str(i)[2] not in str(i)[:2]:] in p[1:]
    #                         or (num[0] in p[0] and num[2] in p[2])]
    #         elif b[1] == 1:
    #             possible = [p for p in possible if num[0] in p[0]
    #                         or num[1] in p[1]
    #                         or num[2] in p[2]]
    #
    #     # ball이라면
    #     if b[2] > 0:
    #         if b[2] == 3:
    #             possible = [p for p in possible if (num[0] in p[1:]) and
    #                         (num[1] in p[0] or num[1] in p[2]) and (num[2] in p[:2])]
    #         elif b[2] == 2:
    #             possible = [p for p in possible if (num[0] in p[1:] and (num[1] in p[0] or num[1] in p[2]))
    #                         or ((num[1] in p[0] or num[1] in p[2]) and (num[2] in p[:2]))
    #                         or ((num[0] in p[1:]) and num[2] in p[:2])]
    #         elif b[2] == 1:
    #             possible = [p for p in possible if num[0] in p[1:]
    #                         or num[1] in p[0]
    #                         or num[1] in p[2]
    #                         or num[2] in p[:2]]
    #
    #     # strike도 ball도 없다면 3 개의 숫자 해당하는 숫자들 제거
    #     if b[1] == 0 and b[2] == 0:
    #         digits = list(str(b[0]))
    #         possible = [p for p in possible if p[0] not in digits and p[1] not in digits and p[2] not in digits]

    # return len(possible)


solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [237, 0, 2], [489, 0, 1]])
