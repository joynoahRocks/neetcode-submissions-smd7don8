class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        if nums[low] < nums[high]:
            return nums[low]
        ans = float('inf')
        while low <= high:
            mid = (low + high)//2
            ans = min(ans,nums[mid])
            if nums[mid] >= nums[0]: #sorted array look min to the right
                low = mid + 1
            else:
                high = mid - 1
        return ans
