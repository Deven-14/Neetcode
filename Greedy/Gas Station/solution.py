class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)

        for j in range(n):
            if cost[j] > gas[j]:
                continue
            
            tank = gas[j] - cost[j]
            i = j + 1 % n

            while i % n != 0 and tank > 0:
                tank += gas[i] - cost[i]
                i += 1
        
            if i % n == 0:
                return j
        
        return -1

        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)

        for j in range(n):
            if cost[j] > gas[j]:
                continue
            
            tank = gas[j] - cost[j]
            i = (j + 1) % n

            while i != j and tank > 0:
                tank += gas[i] - cost[i]
                i = (i + 1) % n
        
            if i == j:
                return j
        
        return -1

        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)

        tank = 0
        start = 0
        for i in range(n):
            tank += (gas[i] - cost[i])
            if tank < 0:  # tank = 0 is also fine coz, if we have gas 4 and then we spend 4, tank is 0, but we reached the next station, so it is valid
                start = i + 1
                tank = 0
        
        return start

        
