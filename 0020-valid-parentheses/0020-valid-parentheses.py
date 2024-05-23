class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        output = []

        for i in s:
            if i in pair:
                output.append(i)
            else:
                if len(output) == 0 or pair[output.pop()] != i:
                    return False
        return False if output else True