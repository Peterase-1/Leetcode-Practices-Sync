class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        prev_time = 0
        
        for pos, spd in cars:
            time = float(target - pos) / spd
            
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets