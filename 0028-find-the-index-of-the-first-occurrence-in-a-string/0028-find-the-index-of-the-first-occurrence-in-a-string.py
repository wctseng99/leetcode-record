class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            output = haystack.find(needle)
            return output
        except:
            return -1