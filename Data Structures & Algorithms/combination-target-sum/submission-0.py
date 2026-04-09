class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(ind,target,sub):
            if target == 0:
                ans.append(sub[:])
                return 
            if target < 0 or ind >= n:
                return

            sub.append(nums[ind])
            helper(ind,target - nums[ind],sub)
            sub.pop()
            helper(ind + 1,target,sub)
        
        ans = []
        n = len(nums)
        helper(0,target,[])
        return ans