class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            # left to right
            output[i] = nums[i-1] * output[i-1]

        right = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            # right to left 
            output[i] = right * output[i]
            right *= nums[i]
            
        return output