class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        water = 0
        temp = 0
        
        while right < len(height):
            l , r = height[left] , height[right]

            if l > r:
                temp += height[right]
                right +=1

            else:
                print(left , right)
                water = max(water , temp)
                left = right
                right = right +1
                temp = 0

        return water