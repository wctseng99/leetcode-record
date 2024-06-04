class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, cur):
            if len(cur) == k:
                result.append(cur[:])
                return 
            
            for i in range(i, n+1):
                cur.append(i)
                backtrack(i+1, cur)
                cur.pop()
        
        backtrack(1, [])
        return result