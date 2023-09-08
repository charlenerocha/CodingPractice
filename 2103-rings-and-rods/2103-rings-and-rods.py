class Solution:
    def countPoints(self, rings: str) -> int:
        # [hasRed, hasGreen, hasBlue]
        
        trackRings = {}
        
        for i in range(1, len(rings), 2):
            col, ind = rings[i-1], rings[i]
            
            if ind not in trackRings:
                trackRings[ind] = set()
                
            if col == 'R':
                trackRings[ind].add('R')
            elif col == 'G':
                trackRings[ind].add('G')
            elif col == 'B':
                trackRings[ind].add('B')
                
        return sum(1 for val in trackRings.values() if len(val) == 3)
        