class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = tuple(sorted(i))
            d.setdefault(s,[]).append(i)
        return list(d.values())