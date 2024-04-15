class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_amount = max(candies)
        return [i + extraCandies >= max_amount for i in candies]