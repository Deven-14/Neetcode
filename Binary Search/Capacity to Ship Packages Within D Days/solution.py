class Solution:

    def count_days_required(self, weights, max_weight):
        days = 1
        curr_weight = 0

        for weight in weights:
            curr_weight += weight
            if curr_weight > max_weight:
                curr_weight = weight
                days += 1
        
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) <= days:
            return max(weights)
        
        min_weight = max(weights)
        max_weight = sum(weights)
        
        l, r = min_weight, max_weight

        while l < r:
            mid = (l + r) // 2
            required_days = self.count_days_required(weights, mid)
            if required_days > days:
                l = mid + 1
            else:
                r = mid

        return l 
