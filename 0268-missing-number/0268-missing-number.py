class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(0,len(nums) + 1):
            if num not in nums:
                return num
        return -1