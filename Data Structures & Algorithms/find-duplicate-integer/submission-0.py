class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while True:
            val = abs(nums[i])
            if nums[val] < 0:
                return val
            nums[val] = -nums[val]
            i = val
        return 0
