# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            elif node.right and node.left:
                return min(1+helper(node.right), 1+helper(node.left))
            elif node.right:
                return 1+helper(node.right)
            else:
                return 1+helper(node.left)
        return helper(root)