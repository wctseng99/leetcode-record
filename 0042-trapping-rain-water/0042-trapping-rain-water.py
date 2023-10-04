class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(height):
            while stack and stack[-1][1] < h:
                lower_index, lower_height = stack.pop()
                if stack:
                    distance = i - stack[-1][0] - 1
                    trapped_height = min(stack[-1][1], h) - lower_height
                    area += distance * trapped_height
            stack.append([i, h])
        return area