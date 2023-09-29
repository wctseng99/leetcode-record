class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = Counter(arr)
        freq = set()

        for num in occur.values():
            if num in freq:
                return False
            freq.add(num)
        return True