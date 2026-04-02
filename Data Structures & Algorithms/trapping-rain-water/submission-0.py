class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n-1
        ans = 0
        lMax = 0
        rMax = 0
        while left < right:
            lMax = max(height[left],lMax)
            rMax = max(height[right],rMax)
            if height[left] < height[right]:
                ans += min(lMax,rMax) - height[left]
                left += 1
            else:
                ans += min(lMax,rMax) - height[right]
                right -= 1
        return ans
