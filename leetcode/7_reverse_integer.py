class Solution:
    def reverse(self, x: int) -> int:
        isPositive = True if x >= 0 else False
        x = int(str(abs(x))[::-1])
        
        if x > (2 ** 31 -1):
            return 0
        return x if isPositive else -x
        