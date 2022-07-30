class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        final = [matrix[0][0]]
        
        i, j = 0, 0
        minI, minJ = 0, 0
        maxI, maxJ = len(matrix) - 1, len(matrix[0]) - 1
        lastI, lastJ = -1, -1
        if maxJ > 1:
            lastI, lastJ = 1, 0
        
        for num in range((maxI + 1) * (maxJ + 1) - 1):
            if i == lastI and j == lastJ:
                minI += 1
                minJ += 1
                maxI -= 1
                maxJ -= 1
                j += 1
                if i != maxI and j != maxJ:
                    lastI += 1
                    lastJ += 1
            elif maxJ == minJ:
                i += 1
            elif maxI == minI:
                j += 1
            elif j == maxJ and i != maxI:
                i += 1
            elif i == maxI and j != minJ:
                j -= 1
            elif i == minI and j != maxJ:
                j += 1
            elif j == minI and i != minI:
                i -= 1
            
            final.append(matrix[i][j])
        
        return final