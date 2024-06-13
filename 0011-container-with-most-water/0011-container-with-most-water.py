class Solution:
    def maxArea(self, height: List[int]) -> int:
        def find_area(l, r):
            return (r - l) * min(height[right], height[left])
        
        left, right = 0, len(height) - 1 
        max_area = find_area(left, right)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            cur_area = find_area(left, right)
            max_area = max(max_area, cur_area)
        return max_area
            