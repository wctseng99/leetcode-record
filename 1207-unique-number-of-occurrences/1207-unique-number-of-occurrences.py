class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = Counter(arr)
        freq = set()
        for i in occur.values():
            if i in freq:
                return False
            freq.add(i)
        return True