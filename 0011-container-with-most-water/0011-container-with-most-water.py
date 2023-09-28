class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        # move two pointers from outside to inside
        while left != right:
            curr_area = (right -left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area