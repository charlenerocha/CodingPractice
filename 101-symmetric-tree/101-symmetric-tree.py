# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def recursiveSearch(leftie, rightie):
            if leftie == None and rightie == None: return True
            if leftie == None or rightie == None: return False 
        
            return leftie.val == rightie.val and recursiveSearch(leftie.left, rightie.right) and recursiveSearch(leftie.right, rightie.left)
        
        return recursiveSearch(root.left, root.right)