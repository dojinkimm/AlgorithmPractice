class Solution:
    def myAtoi(self, s: str) -> int:
        arr = list(map(str,s.strip().split()))
        result = ""
        num = 0
        hasSign = 0
        if  len(arr) == 0:
            return 0
        
        if arr[0][0] == "+" or arr[0][0] == "-":
            result += arr[0][0]
            hasSign = 1
        elif not arr[0][0].isdigit():
            return 0
        
        for i in range(hasSign, len(arr[0])):
            if arr[0][i].isdigit():
                result += arr[0][i]
            else:
                break
            num = int(result)

        if abs(num) > (2**31 - 1):
            if num >= 0:
                return 2147483647
            else:
                return -2147483648
        return num
    