class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        left = 0
        n = len(s)
        right = 0
        while right < n:
            if s[right] in d:
                left = max(left,d[s[right]] + 1)
            d[s[right]] = right
            ans = max(ans,right - left + 1)
            right += 1
        return ans

