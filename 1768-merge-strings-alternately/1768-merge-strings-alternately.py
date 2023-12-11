class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        left, right = 0, 0
        
        while left < len(word1) and right < len(word2):
            res.append(word1[left])
            res.append(word2[right])
            left += 1
            right += 1
        
        if left < len(word1):
            res.append(word1[left:])
        if right < len(word2):
            res.append(word2[right:])
        
        return "".join(res)