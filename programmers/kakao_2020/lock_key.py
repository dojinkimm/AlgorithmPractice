def turn_right(key):
    N = len(key)
    temp = [[0] * N for _ in range(N)]

    reverse_i = N - 1
    for i in range(N):
        for j in range(N):
            temp[j][reverse_i] = key[i][j]
        reverse_i -= 1
    return temp


def is_correct(bg_size, lock, key, start_x, start_y, start, end):
    bg = [[0] * bg_size for _ in range(bg_size)]

    for i in range(len(key)):
        for j in range(len(key)):
            bg[start_y + i][start_x + j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            bg[i][j] += lock[i - start][j - start]
            if bg[i][j] != 1:
                return False

    return True


def unlock(key, lock):
    M = len(key)
    N = len(lock)
    traverse = M - 1 + N
    bg_size = M + (2 * (N - 1))

    for k in range(4):
        for i in range(traverse):
            for j in range(traverse):
                if is_correct(bg_size, lock, key, i, j, M - 1, traverse):
                    return True
        key = turn_right(key)
    return False


def solution(key, lock):
    answer = unlock(key, lock)

    return answer