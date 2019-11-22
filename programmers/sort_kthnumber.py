# k 번째 - 정렬
def solution(array, commands):
    answer = [sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands]
    return answer
