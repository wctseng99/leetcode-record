class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left, right = left + 1, right - 1
                else:     
                    return False

            else:
                left, right = left + (not s[left].isalnum()), right - (not s[right].isalnum())
                    
        return True