class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        
        return profit

# you can use min_stock and max_stock to reduce the time even more

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_stock = prices[0]
        max_stock = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_stock:
                min_stock = prices[i]
                max_stock = min_stock
                
            elif prices[i] > max_stock:
                profit = max(profit, prices[i] - min_stock)
                max_stock = prices[i]
        
        return profit