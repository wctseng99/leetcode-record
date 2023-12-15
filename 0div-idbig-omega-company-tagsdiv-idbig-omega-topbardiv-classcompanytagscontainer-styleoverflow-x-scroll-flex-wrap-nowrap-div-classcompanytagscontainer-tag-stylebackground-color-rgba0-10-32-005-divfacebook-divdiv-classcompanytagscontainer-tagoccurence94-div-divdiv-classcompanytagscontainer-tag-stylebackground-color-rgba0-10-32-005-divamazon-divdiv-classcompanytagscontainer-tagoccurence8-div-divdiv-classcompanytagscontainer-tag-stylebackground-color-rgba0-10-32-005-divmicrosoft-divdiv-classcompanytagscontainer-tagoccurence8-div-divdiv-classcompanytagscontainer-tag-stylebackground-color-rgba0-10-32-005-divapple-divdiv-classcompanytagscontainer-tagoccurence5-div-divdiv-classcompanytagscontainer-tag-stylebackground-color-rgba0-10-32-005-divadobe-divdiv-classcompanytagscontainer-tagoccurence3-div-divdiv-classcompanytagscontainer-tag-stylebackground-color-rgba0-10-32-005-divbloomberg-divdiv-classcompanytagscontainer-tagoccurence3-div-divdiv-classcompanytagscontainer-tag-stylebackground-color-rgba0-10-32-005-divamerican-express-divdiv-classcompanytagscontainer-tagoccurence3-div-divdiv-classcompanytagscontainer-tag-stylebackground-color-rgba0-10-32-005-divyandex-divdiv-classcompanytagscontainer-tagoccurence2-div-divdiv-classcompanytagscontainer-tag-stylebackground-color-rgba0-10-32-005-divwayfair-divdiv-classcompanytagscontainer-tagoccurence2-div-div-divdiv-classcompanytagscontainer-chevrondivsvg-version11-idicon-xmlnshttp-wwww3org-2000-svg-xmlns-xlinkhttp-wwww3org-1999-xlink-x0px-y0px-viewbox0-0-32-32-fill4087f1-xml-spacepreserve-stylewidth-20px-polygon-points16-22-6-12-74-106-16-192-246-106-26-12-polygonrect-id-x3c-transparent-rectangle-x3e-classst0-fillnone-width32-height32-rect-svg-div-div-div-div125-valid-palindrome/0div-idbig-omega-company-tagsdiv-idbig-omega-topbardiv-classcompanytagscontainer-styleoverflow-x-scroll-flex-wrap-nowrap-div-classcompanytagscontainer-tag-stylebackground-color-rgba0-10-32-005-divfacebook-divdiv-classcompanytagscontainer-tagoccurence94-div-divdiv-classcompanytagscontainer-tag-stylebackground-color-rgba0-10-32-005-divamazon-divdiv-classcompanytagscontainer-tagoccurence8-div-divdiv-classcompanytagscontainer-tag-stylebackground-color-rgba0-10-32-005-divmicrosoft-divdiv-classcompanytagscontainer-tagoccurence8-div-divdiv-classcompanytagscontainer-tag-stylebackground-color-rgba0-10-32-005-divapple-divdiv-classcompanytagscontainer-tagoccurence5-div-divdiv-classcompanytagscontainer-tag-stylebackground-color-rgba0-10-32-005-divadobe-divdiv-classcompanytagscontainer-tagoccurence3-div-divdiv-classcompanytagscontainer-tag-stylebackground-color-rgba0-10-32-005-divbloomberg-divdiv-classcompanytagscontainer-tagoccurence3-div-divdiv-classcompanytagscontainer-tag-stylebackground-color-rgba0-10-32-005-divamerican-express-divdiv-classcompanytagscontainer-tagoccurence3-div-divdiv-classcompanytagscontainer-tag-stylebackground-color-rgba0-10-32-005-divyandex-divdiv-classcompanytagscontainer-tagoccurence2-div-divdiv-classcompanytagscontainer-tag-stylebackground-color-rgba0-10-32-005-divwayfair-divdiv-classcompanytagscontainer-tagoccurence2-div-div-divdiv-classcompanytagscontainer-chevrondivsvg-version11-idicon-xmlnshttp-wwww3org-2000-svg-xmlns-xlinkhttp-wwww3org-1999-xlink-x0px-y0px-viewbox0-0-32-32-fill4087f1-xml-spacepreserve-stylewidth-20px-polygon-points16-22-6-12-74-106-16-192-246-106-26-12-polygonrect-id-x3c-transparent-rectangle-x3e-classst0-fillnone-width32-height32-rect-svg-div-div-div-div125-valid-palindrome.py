class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [i for i in s.lower() if i.isalnum()]
        return res == res[::-1]