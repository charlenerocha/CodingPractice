class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
            
        temp = nums.copy()
        nums[0:k] = temp[len(temp)-k:len(temp)]
        nums[k:len(temp)] = temp[0:len(temp)-k]