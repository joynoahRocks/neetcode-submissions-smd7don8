class Solution:
    def climbStairs(self, n: int) -> int:
        # def helper(n):
        #     if n < 0:
        #         return 0
        #     if n <= 1:
        #         return 1
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] =  helper(n - 1) + helper(n-2)
        #     return dp[n]
        dp = [-1] * (n + 1)
        # return helper(n)


        dp[0] = 1
        dp[1] = 1
        for i in range(2,n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]