class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1, cost2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            cost1, cost2 = cost2, cost[i] + min(cost1, cost2)
        return min(cost1, cost2)