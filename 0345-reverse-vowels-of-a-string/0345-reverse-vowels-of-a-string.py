class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        stack = []
        answer = ""
        for i in s:
            if i in vowels:
                stack.append(i)
        for i in s:
            if i in vowels:
                answer += stack.pop()
            else:
                answer += i
        return answer