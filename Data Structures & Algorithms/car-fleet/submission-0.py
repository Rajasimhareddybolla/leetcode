from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
            
        # Group positions and speeds, and sort them descending.
        # This way, the car closest to the target is always at index 0.
        # This eliminates the need for complex loops to find which car is in front.
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        
        fleets = 0
        
        # Simulate time step-by-step until all cars have crossed the target
        while cars:
            # 1. Move every car forward by its speed (simulating 1 unit of time)
            for i in range(len(cars)):
                cars[i][0] += cars[i][1]
                
            # 2. Resolve Collisions
            # Iterate from front to back. If a car behind caught up to or passed 
            # the car in front of it, it joins that car's fleet.
            for i in range(1, len(cars)):
                # cars[i-1] is the car ahead. cars[i] is the car behind.
                if cars[i][0] >= cars[i-1][0]:
                    cars[i][0] = cars[i-1][0] # Fall back to the car ahead's position
                    cars[i][1] = cars[i-1][1] # Slow down to the car ahead's speed
                    
            # 3. Process cars that have reached or passed the target
            active_cars = []
            finished_positions = set()
            
            for pos, spd in cars:
                if pos >= target:
                    # Because we resolved collisions above, cars in the same fleet 
                    # will have the exact same position. A set automatically counts 
                    # identical positions as just 1 fleet.
                    finished_positions.add(pos)
                else:
                    # Keep cars that haven't reached the target yet
                    active_cars.append([pos, spd])
                    
            # Add the number of unique fleets that crossed the target in this time step
            fleets += len(finished_positions)
            
            # Update the cars list for the next time step loop
            cars = active_cars
            
        return fleets