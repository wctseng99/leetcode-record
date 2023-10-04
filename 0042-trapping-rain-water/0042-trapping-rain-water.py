class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        output = 0
        for i, h in enumerate(height):
            while stack and stack[-1][1] < h:
                index, lower_h = stack.pop()
                if stack:
                    distance = i - stack[-1][0] - 1
                    trapped_height = min(h, stack[-1][1]) - lower_h
                    output += distance * trapped_height
            stack.append([i, h])        
        return output