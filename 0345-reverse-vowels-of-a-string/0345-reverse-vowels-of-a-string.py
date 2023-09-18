class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "AaEeIiOoUu"
        stack = []
        output =""

        for char in s:
            if char in vowels:
                stack.append(char)
        for char in s:
            if char in vowels:
                output += stack.pop()
            else:
                output += char

        return output
