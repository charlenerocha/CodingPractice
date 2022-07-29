class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        length = len(digits) - 1
        
        if digits[length] < 9:
            digits[length] += 1
            return digits
        
        index = length
        
        while index >= 0:
            if digits[index] < 9:
                digits[index] += 1
                break
            else:
                digits[index] = 0
                index -= 1
            
        if index < 0:
            temp = [1]
            temp[1:] = digits
            return temp 
        
        return digits
            