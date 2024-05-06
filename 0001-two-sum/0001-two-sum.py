class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        
        for i, val in enumerate(nums):
            if val in pair:
                return [i, pair[val][0]]
            else:
                pair[target - val] = (i, val)
        