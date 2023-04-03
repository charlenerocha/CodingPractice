# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        allLevels = []
        
        def addLevels(currNode, i):
            if currNode == None:
                return
            
            if len(allLevels) < i + 1:
                allLevels.append([])
                
            allLevels[i].append(currNode.val)
            
            if currNode.left:
                addLevels(currNode.left, i+1)
                
            if currNode.right:
                addLevels(currNode.right, i+1)
            
            
        addLevels(root, 0)
        return allLevels