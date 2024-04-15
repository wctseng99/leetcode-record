class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
        }
        
        stack = []
        
        for char in s:
            # open brackets
            if char in pairs:
                stack.append(char)
            # close brackets
            else:
                if len(stack) == 0 or pairs[stack.pop()] != char:
                    return False
                
        return True if len(stack) == 0 else False
            
        