# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def findTarget(nodeToSearch, copiedNodeToSearch):
            if not nodeToSearch:
                return None
            if nodeToSearch is target:
                return copiedNodeToSearch
            
            left = findTarget(nodeToSearch.left, copiedNodeToSearch.left)
            right = findTarget(nodeToSearch.right, copiedNodeToSearch.right)
                
            if left:
                return left
            else:
                return right
        
        return findTarget(original, cloned)
            