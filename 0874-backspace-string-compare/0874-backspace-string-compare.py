class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack

        s_stack, t_stack = [], []

        def isSameString(string, stack):
            for char in string:
                if char.isalpha():
                    stack.append(char)
                else:
                    if not stack:
                        continue
                    stack.pop()
            return stack


        return isSameString(s, s_stack) == isSameString(t, t_stack)