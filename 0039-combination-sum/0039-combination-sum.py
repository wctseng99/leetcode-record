class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def dfs(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                results.append(cur[:])
                return
            
            # contain duplicates
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        
        return results