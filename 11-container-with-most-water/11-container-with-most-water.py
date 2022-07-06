class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        right, left = 0, len(height) - 1
        maxWater = min(height[left], height[right]) * (left - right)
        
        while right < left:
            maxWater = max(maxWater, min(height[left], height[right]) * (left - right))
            
            if height[right] <= height[left]:
                right = right + 1
            else:
                left = left - 1
            
        return maxWater