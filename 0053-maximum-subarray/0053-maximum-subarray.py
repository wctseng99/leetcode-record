class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = -float('inf'), 0

        for i, val in enumerate(nums):
            curr_sum += val
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum