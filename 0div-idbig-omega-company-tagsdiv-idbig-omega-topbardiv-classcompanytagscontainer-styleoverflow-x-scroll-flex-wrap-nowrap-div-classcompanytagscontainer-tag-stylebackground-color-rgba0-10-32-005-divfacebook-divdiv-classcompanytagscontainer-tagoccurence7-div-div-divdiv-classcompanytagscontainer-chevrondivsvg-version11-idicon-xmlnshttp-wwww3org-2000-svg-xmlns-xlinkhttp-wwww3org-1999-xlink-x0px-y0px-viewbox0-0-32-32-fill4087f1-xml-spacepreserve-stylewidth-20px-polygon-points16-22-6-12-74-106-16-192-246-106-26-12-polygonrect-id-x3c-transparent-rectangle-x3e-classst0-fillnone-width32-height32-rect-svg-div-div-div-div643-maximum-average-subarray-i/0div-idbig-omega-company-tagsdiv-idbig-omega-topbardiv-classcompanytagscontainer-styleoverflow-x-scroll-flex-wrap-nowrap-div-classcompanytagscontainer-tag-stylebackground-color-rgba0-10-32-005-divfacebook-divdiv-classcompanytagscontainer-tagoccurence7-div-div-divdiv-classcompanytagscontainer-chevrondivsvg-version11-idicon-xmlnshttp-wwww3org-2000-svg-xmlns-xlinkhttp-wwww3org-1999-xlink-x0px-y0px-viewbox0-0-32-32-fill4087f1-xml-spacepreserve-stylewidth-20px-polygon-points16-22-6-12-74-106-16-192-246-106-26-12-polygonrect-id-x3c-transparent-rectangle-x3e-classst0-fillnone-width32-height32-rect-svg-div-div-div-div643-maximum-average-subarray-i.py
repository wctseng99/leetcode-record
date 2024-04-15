class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        answer = s
        
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]
            answer = max(s, answer)
        
        return answer / k