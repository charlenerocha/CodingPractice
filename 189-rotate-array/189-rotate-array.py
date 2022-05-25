class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def revArray(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start = start + 1
                end = end - 1
        
        k = k % len(nums)
        revArray(nums, 0, len(nums) - 1)
        revArray(nums, 0, k - 1)
        revArray(nums, k, len(nums) - 1)
        