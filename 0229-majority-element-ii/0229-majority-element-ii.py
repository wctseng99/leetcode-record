class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        output = set()
        
        for i in nums:
            freq[i] += 1
            if freq[i] > len(nums)/3:
                output.add(i)
        return list(output)