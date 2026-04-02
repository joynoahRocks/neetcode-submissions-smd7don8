class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        ans = 0
        for price in prices:
            buy = min(price,buy)
            ans = max(ans,price - buy)
        return ans