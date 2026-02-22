class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n

        prev_pair = 0
        for i in range(1, n):
            num, prev = arr[i], arr[i - 1]
            if num == prev:
                continue
            
            dp[i] = 1
            if (num > prev and prev_pair < 0) or (num < prev and prev_pair > 0):
                dp[i] += dp[i - 1]
            
            prev_pair = 1 if num > prev else -1
        
        return max(dp) + 1
