class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(ind,sub):
            if ind == n:
                ans.append(sub[:])
                return 
            
            sub.append(nums[ind])
            helper(ind + 1,sub)
            sub.pop()
            helper(ind + 1,sub)
        ans = []
        n = len(nums)
        helper(0,[])
        return ans