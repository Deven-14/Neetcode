from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)

        @cache
        def dfs(i, amount):
            if amount < 0:
                return 0
            
            if amount == 0:
                return 1

            if i == n:
                return 0
            
            if coins[i] > amount:
                return 0
            
            return dfs(i, amount - coins[i]) + dfs(i + 1, amount)
        
        return dfs(0, amount)
            
# ! RecursionError: maximum recursion depth exceeded

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = [0] * (amount + 1)
        combinations[0] = 1 # for 0 amount, no of ways to achieve that is 0 coins and hence 1 way

        for coin in coins:
            for curr_amt in range(1, amount + 1):
                if coin <= curr_amt:
                    combinations[curr_amt] += combinations[curr_amt - coin]
        
        return combinations[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = [0] * (amount + 1)
        combinations[0] = 1 # for 0 amount, no of ways to achieve that is 0 coins and hence 1 way

        for coin in coins:
            for curr_amt in range(coin, amount + 1):
                combinations[curr_amt] += combinations[curr_amt - coin]
        
        return combinations[amount]


# this will only work if the coins is in the first loop and amount is in the second loop because if we do it the other way around, we will be counting the same combination multiple times
# for example, if we have 2 coins, 3 amount, then we can have 1, 1, 1 and 1, 2 and 2, 1, but if we do it the other way around, we will be counting 1, 1, 1 and 1, 2 twice
# so, we have to make sure that we are counting the combinations only once
