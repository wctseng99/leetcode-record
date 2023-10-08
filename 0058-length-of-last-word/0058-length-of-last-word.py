class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = list(filter(lambda x: x != "", s.split(" ")))
        return len(output[-1])