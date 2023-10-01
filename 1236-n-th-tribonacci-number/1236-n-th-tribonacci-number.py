class Solution:
    def tribonacci(self, n: int) -> int:
        def get_tribonacci(n):
            if tribonacci[n] == -1:
                if n == 0:
                    tribonacci[n] = 0
                elif 0 < n <= 2:
                    tribonacci[n] = 1
                else:
                    tribonacci[n] = get_tribonacci(n-1) + get_tribonacci(n-2) + get_tribonacci(n-3)
            return tribonacci[n]

        tribonacci = [-1] * (n+1)
        return get_tribonacci(n)
