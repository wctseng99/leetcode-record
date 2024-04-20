class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        if target == 0:
            return len(nums)
        
        curr_sum, left, ans = 0, 0, 0
        for right, val in enumerate(nums):
            curr_sum += val
            
            while curr_sum > target and left < right:
                curr_sum -= nums[left]
                left += 1
                
            if curr_sum == target:
                ans = max(ans , (right - left + 1))

        return len(nums) - ans if ans else -1