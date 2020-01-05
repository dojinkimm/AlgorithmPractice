class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isNegative = True  
        if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor >=0):
            isNegative = False
        dividend, divisor = abs(dividend), abs(divisor)
        quotient, temp = 0, 0
        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i
                quotient |= 1 << i
        
        if quotient >= 2**31 and not isNegative:
            quotient = 2**31 -1
        return quotient if not isNegative else -quotient