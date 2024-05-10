class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def backtrack(i, cur):
            if len(cur) == k:
                results.append(cur[:])
                return 
            
            for i in range(i, n + 1):
                cur.append(i)
                backtrack(i+1, cur)
                cur.pop()
                
        backtrack(1, [])
        return results
        
                