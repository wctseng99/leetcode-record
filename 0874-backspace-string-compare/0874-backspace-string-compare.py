class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack

        s_stack, t_stack = [], []
        for i in s:
            if i.isalpha():
                s_stack.append(i)
            else:
                if not s_stack:
                    continue
                s_stack.pop()
        
        for j in t:
            if j.isalpha():
                t_stack.append(j)
            else:
                if not t_stack:
                    continue
                t_stack.pop()

        return s_stack == t_stack