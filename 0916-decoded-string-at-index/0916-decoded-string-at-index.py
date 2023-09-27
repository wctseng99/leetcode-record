class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0
        for char in s:
            if char.isalpha():
               total_length += 1
            else:
                total_length *= int(char)

        for char in reversed(s):
            if char.isalpha():
                if total_length == k or k == 0:
                    return char
                total_length -= 1
            else:
                total_length //= int(char)
                k %= total_length
        return ""
