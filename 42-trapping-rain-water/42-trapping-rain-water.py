class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
#         UNOPTIMIZED SOLUTION
        
#         length = len(height)
#         if length < 3:
#             return 0
        
#         def findMaxLeft(right):
#             maxLeft = right
            
#             for i in range(right + 1, length):
#                 if height[i] > height[maxLeft]:
#                     maxLeft = i
                    
#             return maxLeft
        
        
#         totalHeight = 0
#         maxRight, maxLeft = 0, findMaxLeft(2)
        
#         for i in range(1, length - 1):
#             above = min(height[maxRight], height[maxLeft]) - height[i]
            
#             if above > 0:
#                 totalHeight = totalHeight + above
                
#             if height[i] > height[maxRight]:
#                 maxRight = i
                
#             if i + 1 == maxLeft and i + 1 < length - 1:
#                 maxLeft = findMaxLeft(i + 2)
        
#         return totalHeight


        if len(height) <= 2: return 0
        n = len(height)
        maxLeft, maxRight = height[0], height[n-1]
        left, right = 1, n - 2
        ans = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans