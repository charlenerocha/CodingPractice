class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backTrack(i, subset):
            if i == length:
                final.append(subset)
            else:
                backTrack(i + 1, subset)
                subset = subset + [nums[i]]
                backTrack(i + 1, subset)
        
        length = len(nums)
        final = []
        backTrack(0, [])
        return final