from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)
        
        fleets = 0
        max_time_to_target = 0.0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > max_time_to_target:
                fleets += 1
                max_time_to_target = time
                
        return fleets