class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = longest = current_sum = 0
        
        if target == 0:
            return len(nums)
        
        for right, val in enumerate(nums):
            current_sum += val
            while left < right and current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                longest = max(longest, right-left+1)

        return len(nums) - longest if longest else -1