class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [format(i, 'b').count('1') for i in range(n + 1)]
        return ans
