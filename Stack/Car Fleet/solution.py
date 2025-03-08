class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(reverse=True)

        time = [(target - pos) / spd for (pos, spd) in position_speed]

        print(time)
        stack = [time[0]]
        for i in range(1, len(time)):
            if time[i] > stack[-1]:
                stack.append(time[i])
        
        return len(stack)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(reverse=True)

        fleets = 1
        pos, spd = position_speed[0]
        time_of_fleet = (target - pos) / spd
        for i in range(1, len(position_speed)):
            pos, spd = position_speed[i]
            curr_time = (target - pos) / spd

            if curr_time > time_of_fleet:
                fleets += 1
                time_of_fleet = curr_time
        
        return fleets