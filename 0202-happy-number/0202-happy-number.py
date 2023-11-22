class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        
        while (n != 1):
            if n in seen:
                return False
            seen.add(n)
            digits = [int(i)*int(i) for i in str(n)]
            n = sum(digits)

        return True