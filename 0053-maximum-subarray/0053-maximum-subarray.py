class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = -float("inf"), 0
        
        for val in nums:
            cur_sum += val
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0

            
        return max_sum