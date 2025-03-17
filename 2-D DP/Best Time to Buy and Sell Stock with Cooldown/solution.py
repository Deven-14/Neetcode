class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        s1 = [0] * n # s1 -> s1 (hold, not buying yet), s3 -> s1 (cooldown)
        s2 = [0] * n # s1 -> s2 (buy), s2 -> s2 (hold on to the buy, not selling yet)
        s3 = [0] * n # s2 -> s3 (sell)

        s1[0] = 0 # s1 -> s1 (if we hold) coz we can't cooldown yet (s3 -> s1)
        s2[0] = -prices[0] # s1 -> s2 (if we buy) we'll be in the negative, no profits, s2 -> s2 not yet possible
        s3[0] = float("-inf") # not reachable yet as only one operation first day (either hold on - don't buy, or buy), we didn't reach sell also yet

        for i in range(1, n):
            # consider incoming edges on the state of the automata
            s1[i] = max(s1[i-1], s3[i-1]) # s1[i-1] hold on, s3[i-1] cooldown from s3->s1
            s2[i] = max(s2[i-1], s1[i-1] - prices[i]) # s2[i-1] hold on, s1[i-1] - prices[i] is buy from s1
            s3[i] = s2[i-1] + prices[i] # sell s2 -> s3, only one way
        
        return max(s1[-1], s3[-1]) # either after cooldown or on hold on in s1, not point of buying now i.e. s1-s2, so not included s2
    

# draw the state machine to understand the transitions
# s1 -> s1 (hold, not buying yet)
# s1 -> s2 (buy)
# s2 -> s2 (hold on to the buy, not selling yet)
# s2 -> s3 (sell)
# s3 -> s1 (cooldown)


from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dfs(i, buying):
            if i >= n: # >= coz of i+2
                return 0
            
            if buying:
                profit_on_buying = dfs(i + 1, False) - prices[i] # False, coz after buying we have to sell and cooldown before buying again
                profit_on_not_buying = dfs(i + 1, True) # hold on, or not doing anything or do not buy the current stock
                return max(profit_on_buying, profit_on_not_buying)
            else:
                profit_on_selling = dfs(i + 2, True) + prices[i] # i+2, skip one day for cooldown and then you can start buying again (True)
                profit_on_not_selling = dfs(i + 1, False) # hold on, don't sell yet, check the next day
                return max(profit_on_selling, profit_on_not_selling)
        
        return dfs(0, True)

