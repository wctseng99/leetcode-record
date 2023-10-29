class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [key for key, val in Counter(nums).items() if val == 1][0]