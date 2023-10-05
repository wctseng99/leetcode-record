class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums)/3
        freq = Counter(nums)
        output = []
        
        for i, val in freq.items():
            if val > threshold:
                output.append(i)
        return output