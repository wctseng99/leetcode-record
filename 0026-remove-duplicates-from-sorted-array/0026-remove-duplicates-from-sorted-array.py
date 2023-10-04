class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        appear = set()
        index = 0
        for i, val in enumerate(nums):
            if val not in appear:
                appear.add(val)
                nums[index] = val
                index += 1
        return index
        