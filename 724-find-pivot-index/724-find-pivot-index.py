class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            if leftSum == (total - leftSum - num):
                return i
            leftSum += num
        return -1