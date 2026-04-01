class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
            
        # 1. Find the index of the highest peak
        max_h = 0
        peak_idx = 0
        for i in range(len(height)):
            if height[i] > max_h:
                max_h = height[i]
                peak_idx = i
        
        water = 0
        
        # 2. Left-to-Right Pass (Your original logic)
        # We only go up to the peak_idx
        left = 0
        temp = 0
        for right in range(peak_idx + 1):
            if height[left] > height[right]:
                temp += height[left] - height[right]
            else:
                water += temp
                temp = 0
                left = right
        
        # 3. Right-to-Left Pass (Mirror of your logic)
        # We start from the end and move toward the peak_idx
        right = len(height) - 1
        temp = 0
        for left in range(len(height) - 1, peak_idx - 1, -1):
            if height[right] > height[left]:
                temp += height[right] - height[left]
            else:
                water += temp
                temp = 0
                right = left
                
        return water