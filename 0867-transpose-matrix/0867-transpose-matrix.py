class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # must return a NEW array of size n,m
        # iterate horizonal, paste vertical
        
        transposed_matrix = [[None] * len(matrix) for i in range(len(matrix[0]))]
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                transposed_matrix[i][j] = matrix[j][i]
        
        return transposed_matrix