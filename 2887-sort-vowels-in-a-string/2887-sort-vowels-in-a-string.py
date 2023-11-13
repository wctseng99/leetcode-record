class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_lst = []
        vowels = "AEIOUaeiou"

        for char in s:
            if char in vowels:
                vowel_lst.append(char)
        vowel_lst = sorted(vowel_lst)
        
        idx = 0
        res = []
        for i, char in enumerate(s):
            if char in vowels:
                res.append(vowel_lst[idx])
                idx += 1
            else:
                res.append(char)

        return "".join(res)
