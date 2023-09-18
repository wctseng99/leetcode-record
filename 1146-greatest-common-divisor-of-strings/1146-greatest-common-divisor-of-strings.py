class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ""

        if str1 + str2 != str2 + str1:
            return output

        output = str1[:gcd(len(str1), len(str2))]
        return output