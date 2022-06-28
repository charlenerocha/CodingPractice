class Solution(object):
    def twoSum(self, nums, target):
        trackedNums = {}
        
        for i, num in enumerate(nums):
            if target - num in trackedNums:
                return [i, trackedNums[target - num]]
            trackedNums[num] = i
            