class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # a square is "trapped" if it has a wall on the left and right side
        # i'll create a map of the right wall and then find the left wall
        # any overlap will get added to waterTrapped
        
        waterTrapped = {}
        wall = 0
        
        # find right wall and add the wall in as well
        maxWall = 0
        for i, column in enumerate(height):
            maxWall = max(maxWall, column)  # finds the highest right facing wall
            wall += column                  # adds to the wall pieces that shouldnt be counted
            waterTrapped[i] = maxWall
            
        maxWall = 0
        waterCount = 0
            
        # find left wall
        for i, column in enumerate(height[::-1]):
            maxWall = max(maxWall, column)  # finds the highest left facing wall
            waterCount += min(maxWall, waterTrapped[len(height) - 1 - i])
            
        return waterCount - wall
    


