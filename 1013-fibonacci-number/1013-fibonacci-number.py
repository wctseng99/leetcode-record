class Solution:
    def fib(self, n: int) -> int:

        def fibonacci(n, dp_array):
            if dp_array[n] == -1:
                if n <= 1:
                    dp_array[n] = n
                else:
                    dp_array[n] = fibonacci(n-2, dp_array) + fibonacci(n-1, dp_array)
            return dp_array[n]

        dp_array = [-1] * (n+1)
        return fibonacci(n, dp_array)
        