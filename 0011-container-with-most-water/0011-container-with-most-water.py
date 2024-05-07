class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = (right - left) * min(height[left], height[right])
        
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            cur_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, cur_area)
        return max_area