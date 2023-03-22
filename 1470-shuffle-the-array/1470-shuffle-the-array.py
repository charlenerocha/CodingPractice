class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_nums = list(nums)
        
        for i in range(n):
            shuffled_nums[i * 2] = nums[i]
            shuffled_nums[(i * 2) + 1] = nums[n + i]
    
        return shuffled_nums