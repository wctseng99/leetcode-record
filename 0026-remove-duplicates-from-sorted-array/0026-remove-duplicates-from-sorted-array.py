class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        index = 0
        for val in nums:
            if val not in unique:
                unique.add(val)
                nums[index] = val
                index += 1
        return index