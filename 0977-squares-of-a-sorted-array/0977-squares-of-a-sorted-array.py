class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        idx = len(nums) - 1

        while idx >= 0:
            if abs(nums[left]) > abs(nums[right]):
                res[idx] = nums[left] * nums[left]
                left += 1
            else:
                res[idx] = nums[right] * nums[right]
                right -= 1
                
            idx -= 1

        return res
