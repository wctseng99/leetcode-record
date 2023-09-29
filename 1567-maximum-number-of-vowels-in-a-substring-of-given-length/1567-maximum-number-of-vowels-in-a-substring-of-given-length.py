class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = curr_vowels = left = 0
        vowels = ["a", "e", "i", "o", "u"]

        for right in range(len(s)):
            if s[right] in vowels:
                curr_vowels += 1
            if right >= k:
                if s[left] in vowels:
                    curr_vowels -= 1
                left += 1
            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels