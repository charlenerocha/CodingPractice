class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans.insert(0, nums[right] * nums[right])
                right = right - 1
            else:
                ans.insert(0, nums[left] * nums[left])
                left = left + 1
        
        return ans