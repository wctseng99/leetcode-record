class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        kth_points = []
        heapq.heapify(kth_points)

        for (x, y) in points:
            dis = -(x*x + y*y)
            if len(kth_points) < k:
                heapq.heappush(kth_points, (dis, x, y))
            else:
                heapq.heappushpop(kth_points, (dis, x, y))
        return [(x, y) for (dis, x, y) in kth_points]