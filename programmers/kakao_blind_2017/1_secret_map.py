# My solution

# 10진수를 2진수의 list로 변환하는 함수
def decimal_to_binary(x, n):
    arr = []
    while x>0:
        arr.insert(0,x%2)
        x //=2
    
    while len(arr)<n:
        arr.insert(0,0)
        
    return arr

def solution(n, arr1, arr2):
    answer = []
    arr1 = list(map(lambda x: decimal_to_binary(x, n), arr1))
    arr2 = list(map(lambda x: decimal_to_binary(x, n), arr2))
    
    # 2진수 list를 string 하나로 합치면서 1을 # 0을 공백으로 대체한다
    for i in range(len(arr1)):
        hash = ""
        for j in range(len(arr2)):
            hash += str(arr1[i][j] | arr2[i][j]).replace("1","#").replace("0"," ")
        answer.append(hash)
          
    return answer


# Best solution
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer