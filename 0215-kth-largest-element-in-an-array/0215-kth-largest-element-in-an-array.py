class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_element = []

        for i in nums:
            if len(kth_element) <= len(nums) - k:
                heapq.heappush(kth_element, -i)
            else:
                heapq.heappushpop(kth_element, -i)
        return -kth_element[0]