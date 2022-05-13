# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node):
            if not node:
                return
            helper(node.left)
            myList.append(node.val)
            helper(node.right)
        
        myList = []
        helper(root)
        return myList
        
        
        