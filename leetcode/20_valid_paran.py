class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paran in s:
            if paran in ["(", "{", "["]:
                stack.append(paran)
            else:
                if stack == []:
                    return False
                
                if (paran == ")" and stack[-1] == "(") or (paran == "}" and stack[-1] == "{") or (paran == "]" and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
        
        return True if stack == [] else False
                    
            
        