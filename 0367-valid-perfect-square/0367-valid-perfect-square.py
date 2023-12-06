class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 0, num
        # binary search
        while left <= right:
            mid = (left + right ) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid -1
            elif square < num:
                left = mid + 1
        return False