class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        left_sum, right_sum = 0, sum(nums)

        for i, val in enumerate(nums):
            right_sum -= val
            if left_sum == right_sum:
                return i
            left_sum += val
        return -1


