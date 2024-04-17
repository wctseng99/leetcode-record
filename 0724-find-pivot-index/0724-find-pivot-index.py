class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i, val in enumerate(nums):
            right_sum -= val
            if left_sum == right_sum:
                return i
            left_sum += val
        
        return -1