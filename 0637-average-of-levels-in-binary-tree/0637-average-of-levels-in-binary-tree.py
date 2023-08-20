# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # map with key = int(level) value = pair of sum of ints, number of ints
        
        levelCount = {}
        
        def visitNodes(l, currnode):
            if not levelCount.get(l):
                levelCount[l] = [currnode.val, 1]
            else:
                levelCount[l][0] += currnode.val
                levelCount[l][1] += 1
            
            if currnode.left:
                visitNodes(l+1, currnode.left)
            if currnode.right:
                visitNodes(l+1, currnode.right)
                
        visitNodes(0, root)
        
        # iterate over the map in order and store in final array
        total = []
        for k, v in sorted(levelCount.items()):
            total.append(v[0]/v[1])
        return total