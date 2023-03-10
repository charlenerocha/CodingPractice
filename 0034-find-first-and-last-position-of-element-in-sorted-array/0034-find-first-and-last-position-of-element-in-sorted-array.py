class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # use a binary search approach
        # [5,7,7,8,8,10] -> [F,F,F,T,T,T]
        # when you find the first true, add the indexes into an array until its done!
        
        def found_target(index):
            start, end, lower, higher = index, index, index, index
            
            while start - 1 >= 0 and nums[start - 1] == target:
                start -= 1
                
            while end + 1 < len(nums) and nums[end + 1] == target:
                end += 1
                
            return [start, end]
        
            
        def binary_search(left, right):
            if right >= len(nums) or left < 0 or right < left:
                return [-1, -1]
            
            mid = (right + left) // 2
            
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return found_target(mid)
            
        return binary_search(0, len(nums) - 1)