class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2 or 0 not in nums:
            return
        
        #use something to bring all non zeros to front
        
        replaceMe, follow, countZero = nums.index(0), nums.index(0) + 1, 1
        
        while follow < len(nums):
            if nums[follow] != 0:
                nums[replaceMe] = nums[follow]
                replaceMe = replaceMe + 1
            else:
                countZero = countZero + 1
                
            follow = follow + 1
        
        #make all others zeros
        
        for i in range(countZero):
            nums[replaceMe] = 0
            replaceMe = replaceMe + 1
            
            
        #need a pointer for the first zero, every non zero follow after that is replaced
        #make all things after the last replaceMe + 0 gone
        #[1,3,12,3,12]
        #[1,3,12,0,0]