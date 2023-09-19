class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        heighest = 0
        for i in gain:
            current += i
            heighest = max(heighest, current)
        return heighest