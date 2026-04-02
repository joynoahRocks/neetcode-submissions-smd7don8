class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            k = target - nums[i]
            if k in d:
                return [d[k],i]
            d[nums[i]] = i
        return []