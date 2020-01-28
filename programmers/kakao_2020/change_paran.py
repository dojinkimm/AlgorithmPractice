# 괄호 변환
def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append('(')
        elif s == ')' and stack:
            stack.pop()
        else:
            return False
    return True


def is_equal(string):
    if string.count('(') == string.count(')') and string != '':
        return True
    return False


def recur(p):
    if p == '':
        return ''

    u, v = '', ''
    i = 0
    # u와 v를 나눈다
    while not is_equal(u):
        i += 1
        u = p[:i]
        v = p[i:]
    # u과 올바른 괄호 문자열이면 그대로 둔다
    if is_correct(u):
        u += recur(v)
        return u
    else:
        answer = '('
        answer += recur(v)
        answer += ')'
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == ')':
                u = u[:i] + '(' + u[i + 1:]
            else:
                u = u[:i] + ')' + u[i + 1:]
        answer += u
        return answer


def solution(p):
    if not p:
        return ''

    if is_correct(p):
        return p

    answer = recur(p)

    return answer