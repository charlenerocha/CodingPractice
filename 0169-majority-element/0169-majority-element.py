class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # without use of count, dictionary where key=num, val=count
        # can use the count() fn, would need to iterate through all numbers
        # better option, since we know it appears n/2 times, after iterating through all, its count should be >0
        
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate