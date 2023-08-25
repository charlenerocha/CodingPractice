class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        totalTriplets = 0       # total count
        seen = set(nums)
        
        for num in nums:
            if num - diff in seen and num + diff in seen: 
                totalTriplets += 1
                
        return totalTriplets
    