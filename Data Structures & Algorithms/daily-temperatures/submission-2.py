class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = [] 
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while st and nums[i] >= st[-1][0]:
                st.pop()
            if st:
                ans[i] = st[-1][1] - i
            st.append((nums[i],i))
        return ans