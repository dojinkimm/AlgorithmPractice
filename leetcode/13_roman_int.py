class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        previous = s[0]
        num = roman[s[0]]
        s = s[1:]
        for idx, letter in enumerate(s):
            num += roman[letter]
            if (letter in ["V","X"] and previous == "I") or (letter in ["L","C"] and previous == "X") or (letter in ["D","M"] and previous == "C"):
                num -= (roman[previous]*2)
            previous = letter                
                
        return num
            
        
                    
                    
                
                    
                