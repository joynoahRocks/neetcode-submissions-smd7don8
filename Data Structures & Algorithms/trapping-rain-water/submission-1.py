class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n-1
        lMax = rMax = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= lMax:
                    lMax = height[left]
                else:
                    ans += lMax - height[left]
                left += 1
            else:
                if height[right] >= rMax:
                    rMax = height[right]
                else:
                    ans += rMax - height[right]
                right -= 1 
        return ans