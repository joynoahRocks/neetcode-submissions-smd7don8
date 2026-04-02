class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n-1
        ans = 0
        while left < right:
            h = min(heights[left],heights[right])
            ans = max(ans,h * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans