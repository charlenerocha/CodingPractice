class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        current_row = -1
        count = -1
        
        for i in range(len(mat)):
            current_count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    current_count += 1
            if current_count > count:
                count = current_count
                current_row = i
        
        return [current_row, count]