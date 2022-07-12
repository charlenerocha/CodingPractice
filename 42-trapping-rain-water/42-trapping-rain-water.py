class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        length = len(height)
        if length < 3:
            return 0
        
        totalWater = 0
        maxLeft, maxRight = 0, 0
        left, right = 0, length - 1
        
        while left < right:
            
            if height[left] < height[right]:
                if maxLeft > height[left]:
                    above = maxLeft - height[left]
                    totalWater = totalWater + above
                    
                maxLeft = max(maxLeft, height[left])
                left = left + 1
                
            else:
                if maxRight > height[right]:
                    above = maxRight - height[right]
                    totalWater = totalWater + above
                    
                maxRight = max(maxRight, height[right])
                right = right - 1
                
        
        return totalWater