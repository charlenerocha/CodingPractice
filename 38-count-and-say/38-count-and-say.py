class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        def count(num):
            final = ""
            currentDig = str(num)[0]
            count = 1
            
            for digit in str(num)[1:]:
                
                if digit == currentDig:
                    count += 1
                else:
                    final = final + str(count)
                    final = final + str(currentDig)
                    count = 1
                    currentDig = digit
                    
            final = final + str(count)
            final = final + str(currentDig)
            return final

        
        num = 1
        for i in range(1, n):
            num = count(num)
        
        return str(num)
