class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, cur, total):
            if total == target:
                result.append(cur[:])
                return 
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            backtrack(i, cur, total+candidates[i])
            cur.pop()
            backtrack(i+1, cur, total)
            
        backtrack(0, [], 0)
        return result