# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        mid, lowest, highest = 0, 1, n

        while guess(mid) != 0:
            mid = (highest + lowest) // 2
            if guess(mid) == -1:
                highest = mid - 1
            elif guess(mid) == 1:
                lowest = mid + 1

        return mid