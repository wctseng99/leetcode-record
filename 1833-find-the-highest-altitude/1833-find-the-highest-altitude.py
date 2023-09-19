class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        height = 0
        for i in range(len(gain)):
            height += gain[i]
            altitude.append(height)
        return max(altitude)