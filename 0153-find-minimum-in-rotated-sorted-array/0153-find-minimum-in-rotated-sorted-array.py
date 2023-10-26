class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = float("inf")
        
        while left <= right:
            mid = (left + right) // 2
            min_val = min(min_val, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min_val
            
            