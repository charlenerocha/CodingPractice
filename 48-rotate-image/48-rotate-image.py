class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
    
        for inside in range(n/2):
            for rotate in range(n - 1 - (inside * 2)):

                temp = matrix[0 + inside][0 + inside + rotate]
                matrix[0 + inside][0 + inside + rotate] = matrix[n - inside - 1 - rotate][0 + inside]
                matrix[0 + inside + rotate][n - inside - 1], temp = temp, matrix[0 + inside + rotate][n - inside - 1]
                matrix[n - inside - 1][n - inside - 1 - rotate], temp = temp, matrix[n - inside - 1][n - inside - 1 - rotate]
                matrix[n - inside - 1 - rotate][0 + inside], temp = temp, matrix[n - inside - 1 - rotate][0 + inside]
        
        
                       