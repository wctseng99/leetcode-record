class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        sorted_stones = sorted(stones)
        
        while len(sorted_stones) > 1:
            bigger = sorted_stones.pop()
            smaller = sorted_stones.pop()

            if bigger > smaller:
                sorted_stones.append(bigger - smaller)
                sorted_stones = sorted(sorted_stones)
        
        return sorted_stones[0] if len(sorted_stones) >= 1 else 0

                
                