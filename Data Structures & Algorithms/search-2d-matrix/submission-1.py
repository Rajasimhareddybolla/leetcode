
def bineryserach(nums , target ):

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            top , bottom = 0 , len(matrix)-1

            while top <= bottom:
                mid = (top+bottom)//2
                fi , li = matrix[mid][0] , matrix[mid][-1]
                if fi<=target<=li:
                    break
                elif target > li:
                    top = mid+1
                else:
                    bottom = mid- 1
            print(mid)
            return bineryserach(matrix[mid] , target)