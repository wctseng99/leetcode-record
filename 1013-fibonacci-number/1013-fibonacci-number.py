class Solution:
    def fib(self, n: int) -> int:

        def fibonacci(n):
            if dp_array[n] == -1:
                if n <= 1:
                    dp_array[n] = n
                else:
                    dp_array[n] = fibonacci(n-2) + fibonacci(n-1)
            return dp_array[n]

        dp_array = [-1] * (n+1)
        return fibonacci(n)
        