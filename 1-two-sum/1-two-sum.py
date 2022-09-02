class Solution(object):
    def twoSum(self, nums, target):
        haveNums = {}
        
        for i, num in enumerate(nums):
            if target - num in haveNums:
                return [i, haveNums[target - num]]
            haveNums[num] = i