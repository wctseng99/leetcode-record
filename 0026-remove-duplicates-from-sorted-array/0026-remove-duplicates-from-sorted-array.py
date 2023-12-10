class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_char = len(set(nums))
        unique = set()
        idx = 0
        for i, char in enumerate(nums):
            if char not in unique:
                nums[idx] = char
                idx += 1
                unique.add(char)
            elif len(unique) == nums_char:
                nums[i] = "_"
        
        return nums_char