class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = float('inf')
        appear = {}
        for i, val in enumerate(nums):
            if val in appear:
                res = i - appear[val]
                if res <= k:
                    return True
            appear[val] = i
        return False
        