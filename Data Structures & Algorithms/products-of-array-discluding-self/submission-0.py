class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        n = len(nums)
        for i in range(n - 1):
            pre.append(pre[i] * nums[i])
            suf.append(suf[i] * nums[n-i-1])
        ans = []
        for i in range(n):
            ans.append(pre[i] * suf[n-i-1])
        return ans