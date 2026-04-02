import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        heap = []
        for i,v in d.items():
            heapq.heappush(heap,(v,i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq,num in heap]