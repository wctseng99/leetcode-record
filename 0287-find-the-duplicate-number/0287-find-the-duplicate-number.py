class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appear = set()
        for i in nums:
            if i in appear:
                return i
            appear.add(i)

