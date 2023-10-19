class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack
        s_stack, t_stack = [], []

        def remove_hash(string, stack):
            for char in string:
                if char == "#" and stack:
                    stack.pop()
                elif char.isalpha():
                    stack.append(char)
            return stack

        return remove_hash(s, s_stack) == remove_hash(t, t_stack)