import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(piles,h,mid):
            hour = 0
            for i in piles:
                hour += math.ceil(i/mid)
            return hour <= h

        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            if isPossible(piles,h,mid):
                high = mid - 1
            else:
                low = mid + 1 
        return low