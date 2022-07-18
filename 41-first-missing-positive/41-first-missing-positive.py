class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lowest = 1
        visited = {}
        
        for num in nums:
            if num == lowest:
                lowest = lowest + 1
            
            while lowest in visited:
                lowest = lowest + 1

            visited[num] = num
            
        return lowest

