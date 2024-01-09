class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP approach
        
        add_last = nums[0]
        total = add_last
        
        for i in range(1, len(nums)):
            # last element is either included...
            add_last = nums[i] + max(0, add_last)
            
            # or not included
            total = max(total, add_last)
            
        return total