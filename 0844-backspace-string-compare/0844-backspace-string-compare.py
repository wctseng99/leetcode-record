class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []
        def remove_hash(text, stack):
            for i in text:
                if i == "#" and stack:
                    stack.pop()
                elif i.isalpha():
                    stack.append(i)
            return stack
        
        return remove_hash(s, s_stack) == remove_hash(t, t_stack)
            