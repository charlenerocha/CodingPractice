class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low, high = 0, len(nums)-1
        mid = 0
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid + 1
            
        print mid
        
        if nums[mid] < target:
            return mid+1
        else:
            return mid