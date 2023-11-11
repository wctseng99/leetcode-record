class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        return [num for num, val in sorted(freq.items(), key=lambda x:x[1], reverse=True)][:k]