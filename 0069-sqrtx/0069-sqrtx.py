class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            elif square < x:
                res = mid
                left = mid + 1
        return res