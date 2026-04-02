class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = str(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        ans = []
        for k,v in d.items():
            ans.append(v)
        return ans