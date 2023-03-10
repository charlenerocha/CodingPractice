class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        to_update_index, pointer_index = 0, 0
        k = 0
        
        while pointer_index < len(nums):
            if nums[pointer_index] != val:
                k += 1
                
                nums[to_update_index] = nums[pointer_index]
                to_update_index += 1
                 
            pointer_index += 1
            
        return k