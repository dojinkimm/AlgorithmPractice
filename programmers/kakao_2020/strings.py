# 문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        cnt, ans = 1, 0
        first = s[:i]
        for j in range(i, len(s), i):
            letter = s[j:j + i]
            if letter == first:
                cnt += 1
            else:
                if cnt > 1:
                    ans += len(str(cnt))
                ans += i
                first, cnt = letter, 1
        if cnt > 1:
            ans += len(str(cnt))
        ans += len(first)
        answer = min(answer, ans)

    return answer