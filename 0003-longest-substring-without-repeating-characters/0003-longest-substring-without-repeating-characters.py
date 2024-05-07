class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        chars = set()

        for right in range(len(s)):
            if s[right] in chars:
                while left < right and s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                    
            chars.add(s[right])
            max_length = max(max_length, len(chars))
        
        return max_length
                
            
            