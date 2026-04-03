class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(f"{n:032b}")[::-1]
        return int(n,2)