# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        totalSum = []
        depthSum = []
        
        def dfs(node, depth):
            print "HI"
            if node.left is not None and node.right is not None:
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
            elif node.left is not None:
                dfs(node.left, depth + 1)
            elif node.right is not None:
                dfs(node.right, depth + 1)
            elif node is not None:
                totalSum.append(node.val)
                depthSum.append(depth)
        
        dfs(root, 0)
        mySum = 0
        maxdepth = -1
        
        for i, thing in enumerate(depthSum):
            print i
            print thing
            print mySum
            if thing > maxdepth:
                mySum = totalSum[i]
                maxdepth = thing
            elif thing == maxdepth:
                mySum = mySum + totalSum[i]
            print mySum
            print
       
        print totalSum
        print depthSum
        return mySum