class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        output = " ".join(s)
        return output