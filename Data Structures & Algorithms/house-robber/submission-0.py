class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(ind):
            if ind == 0:
                return nums[0]
            
            if ind < 0:
                return 0

            if dp[ind] != -1:
                return dp[ind]
            left = helper(ind - 1)
            right = helper(ind - 2) + nums[ind]
            dp[ind] = max(left,right)
            return max(left,right)
        

        n = len(nums)
        dp = [-1] * n
        return helper(n - 1)