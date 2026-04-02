import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        d = dict(sorted(d.items(),key = lambda x:x[1],reverse = True ))
        ans = []
        for i,v in d.items():
            ans.append(i)
            k -= 1
            if k == 0:
                break
        return ans