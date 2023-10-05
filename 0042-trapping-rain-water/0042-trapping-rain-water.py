class Solution:
    def trap(self, height: List[int]) -> int:
        peak_index = 0
        for i in range(len(height)):
            if height[i] > height[peak_index]:
                peak_index = i
        
        left_most_bar = 0
        water = 0

        for i in range(peak_index):
            if height[i] > height[left_most_bar]:
                left_most_bar = i
            else:
                water += height[left_most_bar] - height[i]

        right_most_bar = len(height) - 1

        for i in range(len(height)-1, peak_index, -1):
            if height[i] > height[right_most_bar]:
                right_most_bar = i
            else:
                water += height[right_most_bar] - height[i]
                
        return water