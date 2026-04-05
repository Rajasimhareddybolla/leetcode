class Solution:
    def trap(self, height) -> int:
        left = 0
        right = 1
        water = 0
        temp = 0
        
        while right < len(height):
            l , r = height[left] , height[right]
            print(left , right)
            print(l , r)
            print(temp)
            print("----------")
            if l > r:
                temp += l - r
                right +=1

            else:
                water = water + temp
                left = right
                right = right + 1
                temp = 0

        return water
    
