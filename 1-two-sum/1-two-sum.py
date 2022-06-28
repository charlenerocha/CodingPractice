class Solution(object):
    def twoSum(self, nums, target):
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and i is not j:
                    return [i, j]
                
        return -1