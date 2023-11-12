class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        appear = set(nums)
        longest, length = 0, 0

        for i in nums:
            if i - 1 not in appear:
                length = 1
                while i + length in appear:
                    length += 1
                longest = max(longest, length)
        
        return longest