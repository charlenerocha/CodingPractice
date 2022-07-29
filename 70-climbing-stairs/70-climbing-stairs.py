class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        steps = {1:1, 2:2}
        
        def count(num):
            if num in steps:
                return steps[num]
            
            total = count(num - 1) + count(num - 2)
            steps[num] = total
            return total
        
        return count(n)