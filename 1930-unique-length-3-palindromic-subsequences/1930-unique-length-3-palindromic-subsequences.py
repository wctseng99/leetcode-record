class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        chars = set(s)

        for char in chars:
            left = s.find(char)
            right = s.rfind(char)

            if left < right:
                res += len(set(s[left+1:right]))

        return res