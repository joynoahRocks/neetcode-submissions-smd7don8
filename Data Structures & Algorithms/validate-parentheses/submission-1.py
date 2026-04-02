class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(','[','{']
        st = []
        for i in s:
            if i in open:
                st.append(i)
            else:
                if st:
                    if i == ')' and st[-1] == '(':
                        st.pop()
                    elif i == '}' and st[-1] == '{':
                        st.pop()
                    elif i == ']' and st[-1] == '[':
                        st.pop()
                    else:
                        return False
                else:
                    return False
        return not st 