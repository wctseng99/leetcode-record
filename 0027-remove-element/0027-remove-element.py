class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[index] = v
                index += 1
        return index
        