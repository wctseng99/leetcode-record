class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        operations, steps = 0, 0

        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != sorted_nums[i-1]:
                steps += 1
            operations += steps
        
        return operations