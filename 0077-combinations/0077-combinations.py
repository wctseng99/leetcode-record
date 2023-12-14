class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtracking(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return 

            for i in range(start, n+1):
                comb.append(i)
                backtracking(i+1, comb)
                comb.pop()

        res = []
        backtracking(1, [])
        return res
