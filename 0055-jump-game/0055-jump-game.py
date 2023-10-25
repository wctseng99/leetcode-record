class Solution:
    def canJump(self, nums: List[int]) -> bool:

      reachable_idx = 0

      for i, val in enumerate(nums):
        if i > reachable_idx:
          return False
        reachable_idx = max(reachable_idx, i+val)
      
      return True
            