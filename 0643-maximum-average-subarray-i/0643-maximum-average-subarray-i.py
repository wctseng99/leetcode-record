class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = s = sum(nums[:k])
        left = 0
        for right in range(k, len(nums)):
            s += nums[right]
            s -= nums[left]
            max_sum = max(max_sum, s)
            left += 1
        return max_sum / k