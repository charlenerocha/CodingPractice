class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # i is row
        # j is column
        
        iCovered = {}
        jCovered = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in iCovered:
                        iCovered[i] = i
                    if j not in jCovered:
                        jCovered[j] = j
                if i in iCovered:
                    matrix[i][j] = 0
                if j in jCovered:
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in iCovered:
                    matrix[i][j] = 0
                elif j in jCovered:
                    matrix[i][j] = 0
                    
                