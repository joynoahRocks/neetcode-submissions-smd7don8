class Solution:
    def isValid(self, s: str) -> bool:
        d = {')' : '(','}' : '{',']' : '['}
        st = []
        for i in s:
            if i in d:
                if not st or d[i] != st[-1]:
                    return False
                st.pop()
            else:
                st.append(i)
        return not st