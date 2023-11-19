class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        left, sublst_sum = 0, 0 
        max_freq = 0
        
        for right in range(len(sorted_nums)):
            sublst_sum += sorted_nums[right]
            
            while (sorted_nums[right] * (right - left + 1)) - sublst_sum > k:
                sublst_sum -= sorted_nums[left]
                left += 1
            
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq