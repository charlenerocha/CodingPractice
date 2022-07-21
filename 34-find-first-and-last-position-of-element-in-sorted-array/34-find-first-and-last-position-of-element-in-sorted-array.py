class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        mid = len(nums) / 2
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            if nums[mid] == target:
                
                low = mid
                while low - 1 >= 0 and nums[low - 1] == target:
                    low -= 1
                
                high = mid
                while high + 1 < len(nums) and nums[high + 1] == target:
                    high += 1
                
                return [low, high]
            
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                
                mid = (right + left) / 2
        
        return [-1, -1]