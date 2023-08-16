class Solution:
    def isHappy(self, n: int) -> bool:
        # perform this recursively, track numbers that are seen in a map
            # once this loops, we should return false
            
        seenSets = set()
        
        def checkThisNIsHappy(currentN):
            if currentN in seenSets:
                return False
            seenSets.add(currentN)
            
            total = 0
            for c in str(currentN):
                total += int(c) ** 2  
            
            if total == 1:
                return True
            else:
                return checkThisNIsHappy(total)
            
        return checkThisNIsHappy(n)
        
        # 1^2 + 9^2 = 82
        # 8^2 + 2^2 = 68
        # 6^2 + 8^2 = 100
        # 1^2 + 0^2 + 0^2 = 1
        
        # to return true, we need a power of 10
        # rather than just comparing numbers, could also compare sets of numbers