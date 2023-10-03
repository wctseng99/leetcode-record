class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        appear = defaultdict(list)
        output = 0
        for i, num in enumerate(nums):
             appear[num].append(i)
        for num in appear: 
            output += comb(len(appear[num]), 2)

        return output