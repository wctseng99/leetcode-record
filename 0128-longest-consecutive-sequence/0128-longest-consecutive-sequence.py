class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for i in nums_set:
            if i-1 not in nums_set:
                length = 1
                while i + 1 in nums_set:
                    length += 1
                    i += 1
                longest = max(longest, length)
        return longest
                    