class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        max_heap = [-val for val in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            bigger =  - heapq.heappop(max_heap)
            smaller = - heapq.heappop(max_heap)

            if bigger > smaller:
                heapq.heappush(max_heap, -(bigger - smaller))
        
        return - max_heap[0] if len(max_heap) >= 1 else 0
