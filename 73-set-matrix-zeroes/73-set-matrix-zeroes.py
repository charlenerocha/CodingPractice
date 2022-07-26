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
                if matrix[i][j] == 0 and (i not in iCovered or j not in jCovered):
                    
                    for prevI in range(0, i):
                        matrix[prevI][j] = 0
                    
                    for prevJ in range(0, j):
                        matrix[i][prevJ] = 0
                        
                    iCovered[i] = i
                    jCovered[j] = j
                else:  
                    if i in iCovered:
                        matrix[i][j] = 0
                    if j in jCovered:
                        matrix[i][j] = 0
        