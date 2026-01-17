import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = [[f, t, p] for p, f, t in trips]
        heapq.heapify(trips)  
        
        while trips:
            destination = trips[0][1]
            current_trip_passengers = 0

            while trips and trips[0][0] < destination and current_trip_passengers <= capacity:
                f, t, p = heapq.heappop(trips)
                current_trip_passengers += p
                destination = max(destination, t)

            if current_trip_passengers > capacity:
                return False
            
        return True


