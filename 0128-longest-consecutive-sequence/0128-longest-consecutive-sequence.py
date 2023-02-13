class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = 0
        streak = 0
        
        nums.sort()
        
        for num in nums:
            if streak == 0:
                streak += 1
            elif num == currentVal + 1:
                streak += 1
            elif num == currentVal:
                currentVal = num
            else:
                sequence = max(sequence, streak)
                streak = 1
                
            currentVal = num
        
        return max(sequence, streak)