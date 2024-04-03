class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        final = []
        before, after = 1, 1
        
        # multiply from L to R
        for i in range(0, len(nums)):
            final.append(before)
            before = before * nums[i]
        
        # multiply from R to L
        for i in range(len(nums)-1, -1, -1):
            final[i] = final[i] * after
            after = after * nums[i]
            
        return final