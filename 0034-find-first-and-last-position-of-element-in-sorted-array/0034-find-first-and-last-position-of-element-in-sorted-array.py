class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[right] < target or nums[left] > target:
                return [-1, -1]
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
            if nums[left] == nums[right] and nums[left] == target:
                return [left, right]
        return [-1, -1]
