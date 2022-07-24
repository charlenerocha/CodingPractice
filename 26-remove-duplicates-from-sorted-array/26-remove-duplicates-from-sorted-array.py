class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last = nums[0]
        replace = 0
        
        for i in range(1, len(nums)):
            if replace == 0 and nums[i] == last:
                replace = i
            
            if replace != 0 and nums[i] != last:
                nums[replace] = nums[i]
                replace += 1
            
            last = nums[i]
            
        if replace == 0:
            replace = len(nums)
            
        return replace
