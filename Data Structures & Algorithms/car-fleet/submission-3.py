from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [[p ,s ] for p ,s in zip(position  ,speed)]
        fleets = 0
        mtime = 0
        cars.sort(reverse = True)
        for pos , speed in cars :
            time = (target - pos )/ speed
            if time > mtime :
                fleets +=1
                mtime = time

        return fleets

        