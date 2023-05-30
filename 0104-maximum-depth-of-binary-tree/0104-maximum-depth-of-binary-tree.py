# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findLevel(level, node) -> int:
            if node == None:
                return level
            
            maxLeft, maxRight = level, level
            if node.left != None:
                maxLeft = findLevel(level+1,node.left)
            if node.right != None:
                maxRight = findLevel(level+1,node.right)
            return max(maxLeft,maxRight)
            
            
        if root == None: 
            return 0
        return findLevel(1, root)
        
            
            
            