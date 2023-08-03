class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed_elements = 0
        
        while(nums.count(val)):
            nums.remove(val)
            removed_elements += 1
        
        nums = nums[0:len(nums)-removed_elements]