class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        xValDifferent = rec1[2] <= rec2[0] or rec1[0] >= rec2[2]
        yValDifferent = rec1[3] <= rec2[1] or rec1[1] >= rec2[3]
        
        if xValDifferent or yValDifferent:
            return False
        else:
            return True
        