class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # check columns
        for i in range(0, 9):
            
            # reset the visited nums
            nums = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
            
            for j in range(0, 9):
                if board[i][j] != ".":
                    
                    if board[i][j] not in nums:
                        return False

                    if nums[board[i][j]] == 1:
                        return False

                    nums[board[i][j]] = 1
        
        
        # check rows
        for j in range(0, 9):
            
            # reset the visited nums
            nums = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
            
            for i in range(0, 9):
                if board[i][j] != ".":
                    
                    if board[i][j] not in nums:
                        return False

                    if nums[board[i][j]] == 1:
                        return False

                    nums[board[i][j]] = 1
        
        
        # check boxes
        for add1 in range(0, 9, 3):
            for add2 in range(0, 9, 3):

                # reset the visited nums
                nums = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

                for i in range(0 + add1, 3 + add1):
                    for j in range(0 + add2, 3 + add2):
                        
                        if board[i][j] != ".":

                            if board[i][j] not in nums:
                                return False

                            if nums[board[i][j]] == 1:
                                return False

                            nums[board[i][j]] = 1
                        
        return True