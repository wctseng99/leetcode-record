class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies = max(candies)
        for kid in candies:
            return [kid+extraCandies >= maxCandies for kid in candies]