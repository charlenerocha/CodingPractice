class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for 0's
        l, r = 0, 0
        
        while r < len(nums):
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        
        # for 1's
        l, r = l, l
        
        while r < len(nums):
            if nums[r] == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1