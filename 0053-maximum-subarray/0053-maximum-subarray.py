from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [nums[0]]
        total = nums[0]
        
        for i in range(1, len(nums)):
            last = max(nums[i], nums[i] + dp[-1])
            dp.append(last)
    
        return max(dp)
