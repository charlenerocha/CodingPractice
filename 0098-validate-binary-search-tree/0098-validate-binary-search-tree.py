# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMinVal(self, root: Optional[TreeNode]) -> bool:
        while root and root.left:
            root = root.left
        return root.val
    
    def getMaxVal(self, root: Optional[TreeNode]) -> bool:
        while root and root.right:
            root = root.right
        return root.val
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:    return True
        
        isRightBST = True
        if root.right is not None:
            if root.right.val <= root.val:
                return False
            isRightBST = self.isValidBST(root.right)
            minVal = self.getMinVal(root.right)
            if minVal <= root.val:
                return False
        
        isLeftBST = True
        if root.left is not None:
            if root.left.val >= root.val:
                return False
            isLeftBST = self.isValidBST(root.left)
            maxVal = self.getMaxVal(root.left)
            if maxVal >= root.val:
                return False
        
        return isRightBST and isLeftBST