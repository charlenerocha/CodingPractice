class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # fill_in track where we place non-zero numbers
        # chase will iterate through the array
        fill_in, chase = 0, 0

        while chase < len(nums):
            # found a non-zero number
            if nums[chase] != 0:
                nums[fill_in] = nums[chase]
                fill_in += 1

            chase += 1

        # fill in the rest of the array with 0s
        for i in range(fill_in, len(nums)):
            nums[i] = 0


