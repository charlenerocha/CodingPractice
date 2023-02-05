class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        m, n = 0, 0
        
        for move in moves:
            if move == 'R':
                n += 1
            elif move == 'L':
                n = n - 1
            elif move == 'U':
                m += 1
            elif move == 'D':
                m -= 1
            else:
                print("ERR")
        
        return (m == 0 and n == 0)