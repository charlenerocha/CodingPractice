class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        while len(nums) > 0:
            if max(nums) * -1 in nums:
                return max(nums)
            else:
                nums.remove(max(nums))
        return -1