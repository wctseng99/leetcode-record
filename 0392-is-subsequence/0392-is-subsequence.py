class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        i = 0
        for char in t:
            if s[i] == char:
                i += 1
            if i == len(s):
                return True
        return False