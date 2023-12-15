class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                print(s[left], s[right])
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    
                else:     
                    return False

            else:
                if not s[left].isalnum(): 
                    left += 1
                if not s[right].isalnum(): 
                    right -= 1
                    
        return True