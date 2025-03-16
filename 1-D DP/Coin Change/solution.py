class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for curr_amt in range(coin, amount+1):
                if dp[curr_amt - coin] < amount:
                    dp[curr_amt] = min(dp[curr_amt], 1 + dp[curr_amt - coin])
        
        return dp[amount] if dp[amount] != amount+1 else -1