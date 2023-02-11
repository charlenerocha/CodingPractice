class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # 2nd try
        # for water to be "trapped" it needs a left and right wall higher than its own
        highestLeftWall = {}
        maxLeftWall = 0

        # track the leftmost highest wall for each column
        for i, waterLevel in enumerate(height):
            maxLeftWall = max(maxLeftWall, waterLevel)
            highestLeftWall[i] = maxLeftWall

        maxRightWall = 0
        waterTrapped = 0

        # track the rightmost highest wall for each column (and compute the rainwater trapped)
        for i, waterLevel in enumerate(height[::-1]):
            maxRightWall = max(maxRightWall, waterLevel)

            if min(maxRightWall, highestLeftWall[len(height) - 1 - i]) - waterLevel > 0:
                waterTrapped += min(maxRightWall, highestLeftWall[len(height) - 1 - i]) - waterLevel
            
        return waterTrapped