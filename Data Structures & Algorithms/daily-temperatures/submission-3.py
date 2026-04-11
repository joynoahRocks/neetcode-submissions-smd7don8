class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = [] 
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while st and nums[i] >= nums[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans