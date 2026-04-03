class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(n):
            cnt = 0
            for i in range(32):
                if 1 << i & n:
                    cnt += 1
            return cnt
        ans = []
        for i in range(n+1):
            ans.append(countBits(i))
        return ans