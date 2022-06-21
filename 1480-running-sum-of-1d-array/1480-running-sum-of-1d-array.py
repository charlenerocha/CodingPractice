class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sum = 0
        l = len(nums)
        
        for i in range(l):
            sum = sum + nums[i]
            nums[i] = sum
            
        return nums
            
            